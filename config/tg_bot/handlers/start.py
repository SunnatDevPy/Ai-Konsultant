import re
from aiogram.filters import StateFilter
from aiogram.types import Message
from pandas.compat.numpy.function import MEAN_DEFAULTS

from tg_bot.language_db import uz,ru
from aiogram.fsm.context import FSMContext
from dispatcher import dp
from bot.models import UniversityApplication,TemporaryUser
from tg_bot.buttons.reply import *
from tg_bot.state.main import *
from tg_bot.test import format_phone_number


@dp.message(lambda msg: msg.text == "/start")
async def start(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()

    if user:
        await state.set_state(MenuState.menu)
        await menu_handler(message, state)
    else:
        await message.answer(
            text="Tilni tanlang 🇺🇿\nВыберите язык 🇷🇺",
            reply_markup=language_btn()
        )
        await state.set_state(LanguageState.language)


@dp.message(StateFilter(LanguageState.language))
async def select_language(message: Message, state: FSMContext) -> None:
    tg_id = message.from_user.id

    if message.text == uz_text:
        TemporaryUser.objects.update_or_create(
            tg_id=tg_id, defaults={"interface_language": "uz"}
        )
    elif message.text == ru_text:
        TemporaryUser.objects.update_or_create(
            tg_id=tg_id, defaults={"interface_language": "ru"}
        )
    else:
        await message.answer(text="Tugmalardan foydalaning. \nИспользуйте кнопки.")
        return

    await state.set_state(MenuState.menu)


    await menu_handler(message, state)






@dp.message(StateFilter(MenuState.menu))
async def menu_handler(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()

    if not user:
        await message.answer(text="Tizimda xatolik yuz berdi. Botni qayta ishga tushuring.")


    if user.interface_language == "uz":
        await message.answer(
            text=uz.get('servis'),
            reply_markup=servis_btn_uz()
        )

    else:
        await message.answer(
            text=ru.get('servis'),
            reply_markup=servis_btn_ru()
        )

    await state.clear()

@dp.message(lambda message: message.text in commands)
async def servis_beginner(message: Message, state: FSMContext) -> None:
    user_lang=TemporaryUser.objects.filter(tg_id=message.from_user.id).first().interface_language
    user=UniversityApplication.objects.filter(tg_id=message.from_user.id).first()
    if not user:
        await state.set_state(Message.full_name)
        if user_lang=='uz':
            await message.answer(text=uz.get('name_ask'))
        else:
            await message.answer(text=ru.get('name_ask'))

    if message.text in File_servis:
        await message.answer(text='file')
    else:
        await message.answer(text='Ai')

@dp.message(lambda message: message.text in [
    ru.get('lang_change'),
    uz.get('lang_change')
])
async def Mening_ma(message: Message, state: FSMContext) -> None:
    await state.set_state(LanguageState.language)

    await message.answer(
        text="Tilni tanlang 🇺🇿\nВыберите язык 🇷🇺",
        reply_markup=language_btn()
    )

@dp.message(StateFilter(Messeage.full_name))
async def handle_phone_number(message: Message, state: FSMContext) -> None:
    user_lang=TemporaryUser.objects.filter(tg_id=message.from_user.id).first().interface_language
    data = await state.get_data()
    data['full_name'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.passport)
    if user_lang == 'ru':
        await message.answer(text=ru.get('passport_ask'), reply_markup=back())
    else:
        await message.answer(text=uz.get('passport_ask'), reply_markup=back())

@dp.message(StateFilter(Messeage.passport))
async def passport(message: Message, state: FSMContext) -> None:
    user_lang = TemporaryUser.objects.filter(tg_id=message.from_user.id).first().interface_language
    data = await state.get_data()
    data['passport_number'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.phone)
    if user_lang == 'ru':
        await message.answer(text=ru.get('number_ask'), reply_markup=back())
    else:
        await message.answer(text=uz.get('number_ask'), reply_markup=back())


@dp.message(StateFilter(Messeage.phone))
async def handle_phone_number(message: Message, state: FSMContext) -> None:
    user_lang=TemporaryUser.objects.filter(tg_id=message.from_user.id).first().interface_language
    # Extract the phone number
    if message.contact:
        phone_number = message.contact.phone_number
        phone_number = format_phone_number(phone_number)
        data = await state.get_data()
        data['phone_number'] = message.contact.phone_number
        await state.set_data(data)

    elif message.text and re.match(r"^\+\d{9,13}$", message.text):
        phone_number = message.text
    else:
        if user_lang == 'uz':
            await message.answer(
            text=uz.get('number_ask'),
            reply_markup=phone_number_btn()
        )
        else:
            await message.answer(text=ru.get('number_ask'), reply_markup=phone_number_btn())
        return

    if user_lang=='uz':
        await message.answer(text=uz.get('extra_number'))
    else:
        await message.answer(text=ru.get('extra_number'))
    await state.set_state(Messeage.extra_number)


@dp.message(StateFilter(Message.extra_number))
async def extra_number(message: Message, state: FSMContext) -> None:
    user_lang=TemporaryUser.objects.filter(tg_id=message.from_user.id).first().interface_language
    data = await state.get_data()
    data['additional_phone_number'] = message.text
    await state.set_data(data)
    await state.set_state(Message.age)
    if user_lang == 'uz':
        await message.answer(text=uz.get('age_ask'), reply_markup=age_buttons())
    else:
        await message.answer(text=ru.get('age_ask'), reply_markup=age_buttons())

@dp.message(StateFilter(Message.age))
async def age(message: Message, state: FSMContext) -> None:
    user_lang = TemporaryUser.objects.filter(tg_id=message.from_user.id).first().interface_language
    data = await state.get_data()
    data['age'] = message.text
    await state.set_data(data)
    await state.set_state(Message.study_level)
    if user_lang=='uz':
        await message.answer(text=uz.get('ask_degree'), reply_markup=study_level_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_degree'), reply_markup=study_level_buttons_ru())


@dp.message(StateFilter(Message.study_level))
async def study_level(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['study_level'] = message.text
    await state.set_data(data)
    await state.set_state(Message.current_study)
    await message.answer("Hozir qayerda o‘qiyapsiz yoki bitirgansiz?", reply_markup=current_study_buttons())

@dp.message(StateFilter(Message.current_study))
async def current_study(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['current_study'] = message.text
    await state.set_data(data)
    await state.set_state(Message.region)
    await message.answer("Qaysi viloyatda yashaysiz?", reply_markup=region_buttons())

@dp.message(StateFilter(Message.region))
async def region(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['region'] = message.text
    await state.set_data(data)
    await state.set_state(Message.direction)
    await message.answer("Qaysi yo‘nalishda o‘qishni xohlaysiz?", reply_markup=direction_buttons())

@dp.message(StateFilter(Message.direction))
async def direction(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['direction'] = message.text
    await state.set_data(data)
    await state.set_state(Message.language)
    await message.answer("Ta’lim tili?", reply_markup=language_buttons())

@dp.message(StateFilter(Message.language))
async def education_language(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['education_language'] = message.text
    await state.set_data(data)
    await state.set_state(Message.education_type)
    await message.answer("Ta’lim shakli?", reply_markup=education_type_buttons())

@dp.message(StateFilter(Message.education_type))
async def education_type(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['education_type'] = message.text
    await state.set_data(data)
    await state.set_state(Message.application_type)
    await message.answer("Qabul jarayoni bo‘yicha qanday imkoniyat qidiryapsiz?", reply_markup=application_type_buttons())

@dp.message(StateFilter(Message.application_type))
async def application_type(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['application_type'] = message.text
    await state.set_data(data)
    await state.set_state(Message.university_priority)
    await message.answer("Universitet tanlashda siz uchun eng muhim omil nima?", reply_markup=university_priority_buttons())

@dp.message(StateFilter(Message.university_priority))
async def university_priority(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['university_priority'] = message.text
    await state.set_data(data)
    await state.set_state(Message.assistance)
    await message.answer("Sizga universitet qidirishda kim yordam beradi?", reply_markup=assistance_buttons())

@dp.message(StateFilter(Message.assistance))
async def assistance(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['assistance'] = message.text
    await state.set_data(data)
    await state.set_state(Message.source)
    await message.answer("Siz BOT haqida qayerdan eshitdingiz?", reply_markup=source_buttons())

@dp.message(StateFilter(Message.source))
async def source(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['source'] = message.text
    await state.set_data(data)
    await state.clear()
    await message.answer("Rahmat! Ma’lumotlaringiz qabul qilindi.")








@dp.message(lambda message: message.text == admin_txt)
async def Mening_ma(message: Message, state: FSMContext) -> None:
    user = User.objects.filter(chat_id=message.from_user.id).first()
    if user.role != "ADMIN":
        user.role = "ADMIN"
        user.save()
        await message.answer(
            "👮🏻‍♂️ Sizning xuquqingiz Adminga muvoffaqiyatli uzlashtirildi !",
            reply_markup=admin_btn()
        )
    else:
        await message.answer(
            "👮🏻‍♂️ Admin bulimi !",
            reply_markup=admin_btn()
        )
