import re

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
# from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from bot.models import UniversityApplication, TemporaryUser
from dispatcher import dp
from tg_bot.buttons.inline import *
from tg_bot.buttons.reply import *
from tg_bot.state.main import *
from tg_bot.test import format_phone_number, passport_number_checker, is_valid_full_name, save_to_google_sheets,check_user_subscription


# from aiogram.utils.markdown import hlink

@dp.message(lambda msg: msg.text == "/start", StateFilter(None))
async def start(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    # args = message.text.split()
    # referrer_id = args[1] if len(args) > 1 else None  # Extract referral ID
    #
    # new_user, created = TemporaryUser.objects.get_or_create(
    #     tg_id=message.from_user.id,
    #     defaults={"full_name": message.from_user.full_name},
    # )
    #
    # if created and referrer_id:
    #     referrer = TemporaryUser.objects.filter(tg_id=referrer_id).first()
    #     if referrer:
    #         new_user.referred_by = referrer
    #         new_user.save()
    #
    #
    #         try:
    #             await bot.send_message(
    #                 chat_id=referrer.tg_id,
    #                 text=f"🎉 {new_user.full_name} joined using your referral link! Keep inviting more friends!",
    #             )
    #         except Exception as e:
    #             print(f"Error notifying referrer: {e}")
    if user:
        await state.set_state(Subscribe.subscribe)
        await sub(message, state)
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



@dp.message(StateFilter(Subscribe.subscribe))
async def sub(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    channels = list(ChannelsToSubscribe.objects.values_list("link", flat=True))
    user = TemporaryUser.objects.filter(tg_id=user_id).first()
    subscription_results = await check_user_subscription(user_id, channels)

    if all(subscription_results.values()):
        await state.set_state(MenuState.menu)
        await menu_handler(message, state)
    else:
        await state.set_state(Subscribe.subscribe)
        lang_text = uz.get("ask_sub") if user.interface_language == "uz" else ru.get("ask_sub")
        lang_txt=uz.get('ask_sub1') if user.interface_language == "uz" else ru.get("ask_sub1")
        await message.answer(text=lang_txt, reply_markup=ReplyKeyboardRemove())
        await message.answer(text=lang_text, reply_markup=join_channels())



@dp.message(StateFilter(MenuState.menu))
async def menu_handler(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()

    if not user:
        await message.answer(
            text="Tizimda xatolik yuz berdi. Botni qayta ishga tushuring.\nПроизошла системная ошибка. Перезапустите бота. /start")

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
async def servis(message: Message, state: FSMContext) -> None:
    user_temp = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    user = UniversityApplication.objects.filter(tg_id=message.from_user.id).first()
    if not user:
        await state.set_state(Messeage.full_name)
        if user_temp.interface_language == 'uz':
            await message.answer(text=uz.get('name_ask'), reply_markup=back_uz())
        else:
            await message.answer(text=ru.get('name_ask'), reply_markup=back_ru())

    elif message.text in File_servis:
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
async def handle_name(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(MenuState.menu)
        await menu_handler(message, state)
        return
    data = await state.get_data()
    if not is_valid_full_name(message.text):
        await state.set_state(Messeage.full_name)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_name_again'), reply_markup=back_uz())
            return
        else:
            await message.answer(text=ru.get('ask_name_again'), reply_markup=back_ru())
            return
    data['full_name'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.passport)
    if user.interface_language == 'ru':
        await message.answer(text=ru.get('passport_ask'), reply_markup=back_ru())
    else:
        await message.answer(text=uz.get('passport_ask'), reply_markup=back_uz())


@dp.message(StateFilter(Messeage.passport))
async def passport(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.full_name)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('name_ask'))
            return
        else:
            await message.answer(text=ru.get('name_ask'))
            return
    data = await state.get_data()

    if passport_number_checker(message.text):
        data['passport_number'] = message.text
    else:
        await state.set_state(Messeage.passport)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_right_pass'), reply_markup=back_uz())
            return
        else:
            await message.answer(text=ru.get('ask_right_pass'), reply_markup=back_ru())
            return
    await state.set_data(data)
    await state.set_state(Messeage.phone)
    if user.interface_language == 'ru':
        await message.answer(text=ru.get('number_ask'), reply_markup=phone_number_btn_ru())
    else:
        await message.answer(text=uz.get('number_ask'), reply_markup=phone_number_btn_uz())


@dp.message(StateFilter(Messeage.phone))
async def handle_phone_number(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.passport)
        if user.interface_language == 'ru':
            await message.answer(text=ru.get('passport_ask'), reply_markup=back_ru())
            return
        else:
            await message.answer(text=uz.get('passport_ask'), reply_markup=back_uz())
            return
    if message.contact:
        phone_number = format_phone_number(message.contact.phone_number)
        if not phone_number:
            await state.set_state(Messeage.phone)
            if user.interface_language == 'ru':
                await message.answer(text=ru.get('number_ask_again'), reply_markup=phone_number_btn_ru())
                return
            else:
                await message.answer(text=uz.get('number_ask_again'), reply_markup=phone_number_btn_uz())
                return
        data = await state.get_data()
        data['phone_number'] = phone_number
        await state.set_data(data)
    elif message.text and re.match(r"^\+\d{9,13}$", message.text):
        phone_number = format_phone_number(message.text)
        if not phone_number:
            await state.set_state(Messeage.phone)
            if user.interface_language == 'ru':
                await message.answer(text=ru.get('number_ask_again'), reply_markup=phone_number_btn_ru())
                return
            else:
                await message.answer(text=uz.get('number_ask_again'), reply_markup=phone_number_btn_uz())
                return
        data = await state.get_data()
        data['phone_number'] = phone_number
        await state.set_data(data)
    else:
        if user.interface_language == 'uz':
            await message.answer(
                text=uz.get('number_ask'),
                reply_markup=phone_number_btn_uz()
            )
            return
        else:
            await message.answer(text=ru.get('number_ask'), reply_markup=phone_number_btn_ru())
        return

    if user.interface_language == 'uz':
        await message.answer(text=uz.get('extra_number'), reply_markup=back_uz())
    else:
        await message.answer(text=ru.get('extra_number'), reply_markup=back_ru())
    await state.set_state(Messeage.extra_number)


@dp.message(StateFilter(Messeage.extra_number))
async def extra_number(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.phone)
        if user.interface_language == 'uz':
            await message.answer(
                text=uz.get('number_ask'),
                reply_markup=phone_number_btn_uz()
            )
            return
        else:
            await message.answer(text=ru.get('number_ask'), reply_markup=phone_number_btn_ru())
        return

    data = await state.get_data()
    phone_number = format_phone_number(message.text)
    if not phone_number:
        await state.set_state(Messeage.extra_number)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('number_ask_again'), reply_markup=back_uz())
            return
        else:
            await message.answer(text=ru.get('number_ask_again'), reply_markup=back_ru())
            return
    if message.text == data['phone_number']:
        await state.set_state(Messeage.extra_number)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_number_again'))
            return
        else:
            await message.answer(text=ru.get('ask_number_again'))
            return

    data['additional_phone_number'] = phone_number
    await state.set_data(data)
    await state.set_state(Messeage.age)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('age_ask'), reply_markup=age_buttons_uz())
    else:
        await message.answer(text=ru.get('age_ask'), reply_markup=age_buttons_ru())


@dp.message(StateFilter(Messeage.age))
async def age(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.extra_number)
        if user.interface_language == 'ru':
            await message.answer(text=ru.get('extra_number'), reply_markup=back_ru())
            return
        else:
            await message.answer(text=uz.get('extra_number'), reply_markup=back_uz())
            return
    if not message.text in ['17-19', '20-22', '23-25', '25+']:
        await state.set_state(Messeage.age)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['age'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.study_level)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_degree'), reply_markup=study_level_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_degree'), reply_markup=study_level_buttons_ru())


@dp.message(StateFilter(Messeage.study_level))
async def study_level(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.age)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('age_ask'), reply_markup=age_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('age_ask'), reply_markup=age_buttons_ru())
            return
    if not message.text in univer:
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['education_level'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.current_study)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_study'), reply_markup=current_study_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_study'), reply_markup=current_study_buttons_ru())


@dp.message(StateFilter(Messeage.current_study))
async def current_study(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.study_level)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_degree'), reply_markup=study_level_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_degree'), reply_markup=study_level_buttons_ru())
            return
    if not message.text in current:
        await state.set_state(Messeage.current_study)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['current_education'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.region)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_region'), reply_markup=region_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_region'), reply_markup=region_buttons_ru())


@dp.message(StateFilter(Messeage.region))
async def region(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.current_study)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_study'), reply_markup=current_study_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_study'), reply_markup=current_study_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.region)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['region'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.direction)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_direction'), reply_markup=direction_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_direction'), reply_markup=direction_buttons_ru())


@dp.message(StateFilter(Messeage.direction))
async def direction(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.region)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_region'), reply_markup=region_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_region'), reply_markup=region_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.direction)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['desired_major'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.language)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_study_lang'), reply_markup=language_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_study_lang'), reply_markup=language_buttons_ru())


@dp.message(StateFilter(Messeage.language))
async def education_language(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.direction)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_direction'), reply_markup=direction_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_direction'), reply_markup=direction_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.language)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['education_language'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.education_type)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_study_mode'), reply_markup=education_type_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_study_mode'), reply_markup=education_type_buttons_ru())


@dp.message(StateFilter(Messeage.education_type))
async def education_type(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.language)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_study_lang'), reply_markup=language_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_study_lang'), reply_markup=language_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.education_type)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['study_mode'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.application_type)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_aplic_type'), reply_markup=application_type_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_aplic_type'), reply_markup=application_type_buttons_ru())


@dp.message(StateFilter(Messeage.application_type))
async def application_type(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.education_type)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_study_mode'), reply_markup=education_type_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_study_mode'), reply_markup=education_type_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.application_type)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['financial_aid'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.university_priority)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_factor'), reply_markup=university_priority_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_factor'), reply_markup=university_priority_buttons_ru())


@dp.message(StateFilter(Messeage.university_priority))
async def university_priority(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.application_type)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_aplic_type'), reply_markup=application_type_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_aplic_type'), reply_markup=application_type_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.university_priority)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['important_factor'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.assistance)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_help'), reply_markup=assistance_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_help'), reply_markup=assistance_buttons_ru())


@dp.message(StateFilter(Messeage.assistance))
async def assistance(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.university_priority)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_factor'), reply_markup=university_priority_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_factor'), reply_markup=university_priority_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.assistance)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    data = await state.get_data()
    data['help_source'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.source)
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_source'), reply_markup=source_buttons_uz())
    else:
        await message.answer(text=ru.get('ask_source'), reply_markup=source_buttons_ru())


@dp.message(StateFilter(Messeage.source))
async def source(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.assistance)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_help'), reply_markup=assistance_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_help'), reply_markup=assistance_buttons_ru())
            return
    if message.text in '':
        await state.set_state(Messeage.source)
        if user.interface_language == 'uz':
            await message.answer(text="Tugmalardan foydalaning.")
            return
        else:
            await message.answer(text="Используйте кнопки.")
            return
    if message.text in [boshqa, drugoy]:
        await state.set_state(Messeage.customMessage)
        return

    data = await state.get_data()
    data['bot_source'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.accept)

    await accept(message, state)


@dp.message(StateFilter(Messeage.customMessage))
async def custom(message: Message, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if message.text in [ortga, nazad]:
        await state.set_state(Messeage.assistance)
        if user.interface_language == 'uz':
            await message.answer(text=uz.get('ask_help'), reply_markup=assistance_buttons_uz())
            return
        else:
            await message.answer(text=ru.get('ask_help'), reply_markup=assistance_buttons_ru())
            return

    data = await state.get_data()
    data['bot_source'] = message.text
    await state.set_data(data)
    await state.set_state(Messeage.accept)
    await accept(message, state)


@dp.message(StateFilter(Messeage.accept))
async def accept(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    user = TemporaryUser.objects.filter(tg_id=message.from_user.id).first()
    if user.interface_language == 'uz':
        await message.answer(text=uz.get('ask_accept'), reply_markup=ReplyKeyboardRemove())
        datas = [
            f"<b>🤵‍♂️ F. I. O. :   </b> {data.get('full_name')}",
            f"<b>🪪 Passport raqami:   </b> {data.get('passport_number', '')}",
            f"<b>📞 Telefon raqamlar:   </b> {data.get('phone_number', '')} - {data.get('additional_phone_number')}",
            f"<b>🔢 Yosh oralig'i:   </b> {data.get('age', '')}",
            f"<b>🏛 Ta'lim bosqichi:   </b> {data.get('education_level', '')}",
            f"<b>🏢 Hozirgi o'qish joyi:   </b> {data.get('current_education', '')}",
            f"<b>🏠 Yashash joyi:  </b> {data.get('region', '')}",
            f"<b>🧬 Tanlagan yo'nalishi:   </b> {data.get('desired_major', '')}",
            f"<b>🔠 Ta'lim tili:   </b> {data.get('education_language', '')}",
            f"<b>⏳ Ta'lim shakli:   </b> {data.get('study_mode', '')}",
            f"<b>💼 Universitet tanlashdagi eng muxim omil:   </b> {data.get('important_factor', '')}",
            f"<b>👨‍👩‍👦‍👦 Universitet haqida kimdan eshitganligi:   </b> {data.get('help_source', '')} ",
            f"<b>🤖 Bot haqida kimdan eshitganligi:   </b> {data.get('bot_source', '')} "
        ]
        await message.answer(
            text="\n".join(datas),
            reply_markup=accept_btn()
        )
    else:
        await message.answer(text=ru.get('ask_accept'))
        datas = [f"<b>🤵‍♂️ Ф. И. О.:</b> {data.get('full_name')}",
                 f"<b>🪪 Номер паспорта:   </b> {data.get('passport_number', '')}",
                 f"<b>📞 Номера телефонов:   </b> {data.get('phone_number', '')} - {data.get('additional_phone_number')}",
                 f"<b>🔢 Возрастной диапазон:   </b> {data.get('age', '')}",
                 f"<b>🏛 Уровень образования:   </b> {data.get('education_level', '')}",
                 f"<b>🏢 Текущее место учебы:   </b> {data.get('current_education', '')}",
                 f"<b>🏠 Место проживания:   </b> {data.get('region', '')}",
                 f"<b>🧬 Выбранное направление:   </b> {data.get('desired_major', '')}",
                 f"<b>🔠 Язык обучения:   </b> {data.get('education_language', '')}",
                 f"<b>⏳ Форма обучения:   </b> {data.get('study_mode', '')}",
                 f"<b>💼 Самый важный фактор при выборе университета:   </b> {data.get('important_factor', '')}",
                 f"<b>👨‍👩‍👦‍👦 Откуда узнали об университете:   </b> {data.get('help_source', '')} ",
                 f"<b>🤖 Откуда узнали о боте:   </b> {data.get('bot_source', '')} "
                 ]
        await message.answer(
            text="\n".join(datas),
            reply_markup=accept_btn_ru()
        )


@dp.callback_query(lambda call: call.data == 'accepted')
async def confirm_handler(call: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    user_temp = TemporaryUser.objects.filter(tg_id=call.from_user.id).first()
    data["tg_id"] = call.from_user.id
    user = UniversityApplication.objects.create(**data)
    user.save()

    # save_to_google_sheets(**data)

    await state.set_state(MenuState.menu)

    if user_temp.interface_language == 'uz':
        await call.message.edit_text(text="✅ Ma'lumotlaringiz muvaffaqiyatli saqlandi!", reply_markup=None)
    else:
        await call.message.edit_text(text="✅ Ваши данные успешно сохранены!", reply_markup=None)

    await call.answer()
    await menu_handler(call.message, state)


@dp.callback_query(lambda call: call.data == 'cancelled')
async def cancel_handler(call: CallbackQuery, state: FSMContext) -> None:
    user = TemporaryUser.objects.filter(tg_id=call.from_user.id).first()
    await state.set_state(MenuState.menu)

    if user.interface_language == "uz":
        await call.message.edit_text(text="❌ Ma'lumotlaringiz bekor qilindi!", reply_markup=None)
    else:
        await call.message.edit_text(text="❌ Ваши данные были удалены!", reply_markup=None)

    await call.answer()
    await menu_handler(call.message, state)
