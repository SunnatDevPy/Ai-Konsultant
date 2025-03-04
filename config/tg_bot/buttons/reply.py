from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.models import  StudyDirections
from tg_bot.buttons.text import *
from tg_bot.language_db import uz,ru



def menu_btn():
    k2 = KeyboardButton(text = orders_list_txt)
    design = [
        [k2],
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)

def phone_number_btn_uz():
    keyboard1=KeyboardButton(text = "Raqamni yuborish 📞",request_contact=True)
    keyboard2=KeyboardButton(text=ortga)
    design=[[keyboard1],[keyboard2]]
    return ReplyKeyboardMarkup(keyboard=design ,
                               resize_keyboard=True)
def phone_number_btn_ru():
    keyboard1 = KeyboardButton(text="Отправить номер 📞", request_contact=True)
    keyboard2 = KeyboardButton(text=nazad)
    design = [[keyboard1], [keyboard2]]
    return ReplyKeyboardMarkup(keyboard=design,
                               resize_keyboard=True)
def language_btn():
    keyboard1 = KeyboardButton(text=uz_text)
    keyboard2 = KeyboardButton(text=ru_text)
    design = [[keyboard1, keyboard2]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def servis_btn_uz():
    keyboard1=KeyboardButton(text=uz.get('servis_btn1'))
    keyboard2=KeyboardButton(text=uz.get('servis_btn2'))
    keyboard3=KeyboardButton(text=uz.get('lang_change'))
    design = [
        [keyboard1],
        [keyboard2],
        [keyboard3],
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def servis_btn_ru():
    keyboard1=KeyboardButton(text=ru.get('servis_btn1'))
    keyboard2=KeyboardButton(text=ru.get('servis_btn2'))
    keyboard3 = KeyboardButton(text=ru.get('lang_change'))
    design = [
        [keyboard1],
        [keyboard2],
        [keyboard3],
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def age_buttons():
    keyboard1=KeyboardButton(text='17-19')
    keyboard2=KeyboardButton(text='20-22')
    keyboard3=KeyboardButton(text='23-25')
    keyboard4=KeyboardButton(text='25+')
    keyboard5=KeyboardButton(text=ortga)
    design = [[keyboard1, keyboard2],[keyboard3, keyboard4],[keyboard5]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def study_level_buttons_uz():
    keyboard1=KeyboardButton(text='Bakalavriat')
    keyboard2=KeyboardButton(text='Magistratura')
    keyboard3 = KeyboardButton(text=ortga)
    design = [[keyboard1, keyboard2], [keyboard3]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def study_level_buttons_ru():
    keyboard1=KeyboardButton(text='Бакалавриат')
    keyboard2=KeyboardButton(text='Степень магистра')
    keyboard3=KeyboardButton(text=nazad)
    design=[[keyboard1, keyboard2],[keyboard3]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def current_study_buttons_uz():
    keyboard1=KeyboardButton(text='Maktab')
    keyboard2=KeyboardButton(text='Litsey/Kollej')
    keyboard3=KeyboardButton(text='Universitet')
    keyboard4 = KeyboardButton(text=ortga)
    design = [[keyboard1, keyboard2], [keyboard3, keyboard4]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def current_study_buttons_ru():
    keyboard1=KeyboardButton(text='Школа')
    keyboard2=KeyboardButton(text='Средняя школа/колледж')
    keyboard3=KeyboardButton(text='Университет')
    keyboard4=KeyboardButton(text=nazad)
    design = [[keyboard1, keyboard2], [keyboard3,keyboard4]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def region_buttons_uz():
    keyboard14 = KeyboardButton(text="Toshkent shahri")
    keyboard1 = KeyboardButton(text="Toshkent viloyati")
    keyboard2 = KeyboardButton(text="Andijon viloyati")
    keyboard3 = KeyboardButton(text="Fargʻona viloyati")
    keyboard4 = KeyboardButton(text="Namangan viloyati")
    keyboard5 = KeyboardButton(text="Samarqand viloyati")
    keyboard6 = KeyboardButton(text="Buxoro viloyati")
    keyboard7 = KeyboardButton(text="Xorazm viloyati")
    keyboard8 = KeyboardButton(text="Navoiy viloyati")
    keyboard9 = KeyboardButton(text="Qashqadaryo viloyati")
    keyboard10 = KeyboardButton(text="Surxondaryo viloyati")
    keyboard11 = KeyboardButton(text="Jizzax viloyati")
    keyboard12 = KeyboardButton(text="Sirdaryo viloyati")
    keyboard13 = KeyboardButton(text="Qoraqalpogʻiston Respublikasi")
    keyboard15=KeyboardButton(text=ortga)

    design=[[keyboard14,keyboard1],
            [keyboard2,keyboard3],
            [keyboard4,keyboard5],
            [keyboard6,keyboard7],
            [keyboard8,keyboard9],
            [keyboard10,keyboard11],
            [keyboard12,keyboard13],
            [keyboard15]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def region_buttons_ru():
    keyboard14 = KeyboardButton(text="Город Ташкент")
    keyboard1 = KeyboardButton(text="Ташкентская область")
    keyboard2 = KeyboardButton(text="Андижанская область")
    keyboard3 = KeyboardButton(text="Ферганская область")
    keyboard4 = KeyboardButton(text="Наманганская область")
    keyboard5 = KeyboardButton(text="Самаркандская область")
    keyboard6 = KeyboardButton(text="Бухарская область")
    keyboard7 = KeyboardButton(text="Хорезмская область")
    keyboard8 = KeyboardButton(text="Навоийская область")
    keyboard9 = KeyboardButton(text="Кашкадарьинская область")
    keyboard10 = KeyboardButton(text="Сурхандарьинская область")
    keyboard11 = KeyboardButton(text="Джизакская область")
    keyboard12 = KeyboardButton(text="Сырдарьинская область")
    keyboard13 = KeyboardButton(text="Республика Каракалпакстан")
    keyboard15=KeyboardButton(text=nazad)
    design = [[keyboard14, keyboard1],
              [keyboard2, keyboard3],
              [keyboard4, keyboard5],
              [keyboard6, keyboard7],
              [keyboard8, keyboard9],
              [keyboard10, keyboard11],
              [keyboard12, keyboard13],
              [keyboard15]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def direction_buttons_uz():
    # directions = StudyDirections.objects.all()
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # for direction in directions:
    #     keyboard.add(KeyboardButton(text=direction.title))
    # return keyboard
    keyboard1=KeyboardButton(text='test')
    design=[[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)


def direction_buttons_ru():
    keyboard1 = KeyboardButton(text='test')
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def language_buttons():
    keyboard1=KeyboardButton(text="🇺🇿 O‘zbek")
    keyboard2=KeyboardButton(text="🇷🇺 Русский")
    keyboard3=KeyboardButton(text="🇺🇸 English")
    keyboard4=KeyboardButton(text=ortga)
    design=[[keyboard1,keyboard2],[keyboard3,keyboard4]]
    return ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)

def education_type_buttons_uz():
    keyboard1 = KeyboardButton(text="Kunduzgi")
    keyboard2 = KeyboardButton(text="Kechki")
    keyboard3 = KeyboardButton(text="Sirtqi")
    keyboard4 = KeyboardButton(text="Masofaviy")
    keyboard5 = KeyboardButton(text=ortga)
    design = [[keyboard1, keyboard2], [keyboard3, keyboard4],[keyboard5]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def education_type_buttons_ru():
    keyboard1 = KeyboardButton(text="Дневное время")
    keyboard2 = KeyboardButton(text=".")
    keyboard3 = KeyboardButton(text="Внешне")
    keyboard4 = KeyboardButton(text="Удаленный")
    keyboard5 = KeyboardButton(text=nazad)
    design = [[keyboard1, keyboard2], [keyboard3, keyboard4], [keyboard5]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def application_type_buttons_uz():
    keyboard1=KeyboardButton(text="Grant")
    keyboard2=KeyboardButton(text="Kontrakt")
    keyboard3=KeyboardButton(text="Ikkalasiga ham topshiraman")
    design=[[keyboard1,keyboard2],[keyboard3]]
    return ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
def application_type_buttons_ru():
    keyboard1 = KeyboardButton(text="Грант")
    keyboard2 = KeyboardButton(text="Kонтракт")
    keyboard3 = KeyboardButton(text="Я подчиняюсь обоим")
    keyboard4=KeyboardButton(text=ortga)
    design = [[keyboard1, keyboard2], [keyboard3,keyboard4]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def university_priority_buttons_uz():
    keyboard1=KeyboardButton(text="Joylashuv")
    keyboard2=KeyboardButton(text="Kontrakt narxi")
    keyboard3=KeyboardButton(text="Ta’lim sifati")
    keyboard4=KeyboardButton(text="Grant imkoniyatlari")
    keyboard5=KeyboardButton(text="Xalqaro diplom")
    keyboard6=KeyboardButton(text="Universitet obro‘si")
    keyboard7=KeyboardButton(text=ortga)
    design=[[keyboard1,keyboard2],[keyboard3,keyboard4],[keyboard5,keyboard6],[keyboard7]]
    return ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
def university_priority_buttons_ru():
    keyboard1 = KeyboardButton(text="Расположение")
    keyboard2 = KeyboardButton(text="Цена контракта")
    keyboard3 = KeyboardButton(text="Качество образования")
    keyboard4 = KeyboardButton(text="Возможности стипендии")
    keyboard5 = KeyboardButton(text="Международный диплом")
    keyboard6 = KeyboardButton(text="Репутация университета")
    keyboard7 = KeyboardButton(text=nazad)
    design = [[keyboard1, keyboard2], [keyboard3, keyboard4], [keyboard5, keyboard6], [keyboard7]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def assistance_buttons_uz():
    keyboard1=KeyboardButton(text="O‘zim mustaqil qaror qilaman")
    keyboard2=KeyboardButton(text="Ota-onam")
    keyboard3=KeyboardButton(text="Ustozlarim")
    keyboard4=KeyboardButton(text="Do‘stlarim")
    keyboard5=KeyboardButton(text=ortga)
    design=[[keyboard1],[keyboard2,keyboard3],[keyboard4,keyboard5]]
    return ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
def assistance_buttons_ru():
    keyboard1 = KeyboardButton(text="Я принимаю свое самостоятельное решение")
    keyboard2 = KeyboardButton(text="Мои родители")
    keyboard3 = KeyboardButton(text="Мои учителя")
    keyboard4 = KeyboardButton(text="Мои друзья")
    keyboard5 = KeyboardButton(text=nazad)
    design = [[keyboard1], [keyboard2, keyboard3], [keyboard4, keyboard5]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def source_buttons_uz():
    keyboard1 = KeyboardButton(text="Instagram")
    keyboard2 = KeyboardButton(text="Telegram")
    keyboard3 = KeyboardButton(text="Google / Yandex")
    keyboard4 = KeyboardButton(text="Do‘stim tavsiya qildi")
    keyboard5 = KeyboardButton(text="Boshqa")
    keyboard6 = KeyboardButton(text=ortga)
    design = [[keyboard1,keyboard2], [keyboard3, keyboard4], [keyboard5, keyboard6]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def source_buttons_ru():
    keyboard1 = KeyboardButton(text="Инстаграм")
    keyboard2 = KeyboardButton(text="Телеграм")
    keyboard3 = KeyboardButton(text="Google/Яндекс")
    keyboard4 = KeyboardButton(text="Мой друг рекомендовал это")
    keyboard5 = KeyboardButton(text="Другой")
    keyboard6 = KeyboardButton(text=nazad)
    design = [[keyboard1, keyboard2], [keyboard3, keyboard4], [keyboard5, keyboard6]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def back_uz():
    keyboard1 = KeyboardButton(text = ortga)
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)
def back_ru():
    keyboard1 = KeyboardButton(text = nazad)
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)





