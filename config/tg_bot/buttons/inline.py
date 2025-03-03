from aiofiles.os import access

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async

from tg_bot.buttons.text import ortga


def accept():
    accept = InlineKeyboardButton(text="✅ Ma'lumotlarni tasdiqlash", callback_data="accepted")
    cancel = InlineKeyboardButton(text = "🗑 Ma'lumotlarni bekor qilish", callback_data="cancelled")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])
def accept1():
    accept = InlineKeyboardButton(text="✅ Ma'lumotlarni tasdiqlash", callback_data="accepted1")
    cancel = InlineKeyboardButton(text = "🗑 Ma'lumotlarni bekor qilish", callback_data="cancelled1")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])

def admin_accept(chat_id):
    accept = InlineKeyboardButton(text="✅ Ma'lumotlarni tasdiqlash", callback_data=f"accepted:{chat_id}")
    cancel = InlineKeyboardButton(text = "🗑 Ma'lumotlarni bekor qilish", callback_data=f"cancelled:{chat_id}")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])

def excel():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Excel",callback_data="Excel")]
    ])
    return keyboard

def yes_no():
    keyword = InlineKeyboardButton(text="Ha", callback_data="yes")
    keyword2 = InlineKeyboardButton(text="Yo'q", callback_data="no")
    return InlineKeyboardMarkup(inline_keyboard=[[keyword], [keyword2]])

def yes_no1():
    keyword = InlineKeyboardButton(text="Ha", callback_data="yes1")
    keyword2 = InlineKeyboardButton(text="Yo'q", callback_data="no1")
    return InlineKeyboardMarkup(inline_keyboard=[[keyword], [keyword2]])





def reply_inline(user):
    keyboard = InlineKeyboardButton(text="Qo'shimcha bonus qo'shish",callback_data=f"bonus_adding:{user.chat_id}")
    keyboard2 = InlineKeyboardButton(text="Qo'shimcha jarima qo'shish",callback_data=f"expense_adding:{user.chat_id}")
    keyboard4 = InlineKeyboardButton(text="Yangi natija qo'shish",callback_data=f"result_adding:{user.chat_id}")
    ortiga = InlineKeyboardButton(text=ortga, callback_data=ortga)
    return InlineKeyboardMarkup(inline_keyboard=[[keyboard],[keyboard2],[keyboard4],[ortiga]])