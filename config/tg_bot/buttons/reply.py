from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.models import  UniversityApplication
from tg_bot.buttons.text import *
from tg_bot.language_db import uz,ru



def menu_btn():
    k2 = KeyboardButton(text = orders_list_txt)
    design = [
        [k2],
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)

def phone_number_btn():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Raqamni yuborish 📞",
                                                         request_contact=True) ]] ,
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
    design = [[keyboard1, keyboard2],[keyboard3, keyboard4]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def study_level_buttons_uz():
    keyboard1=KeyboardButton(text='Bakalavriat')
    keyboard2=KeyboardButton(text='Magistratura')
    design=[[keyboard1, keyboard2]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
def study_level_buttons_ru():
    keyboard1=KeyboardButton(text='Бакалавриат')
    keyboard2=KeyboardButton(text='Степень магистра')
    design=[[keyboard1, keyboard2]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)








def back():
    keyboard1 = KeyboardButton(text = ortga)
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)





