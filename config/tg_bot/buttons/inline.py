from aiofiles.os import access

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tg_bot.buttons.text import ortga, nazad


def accept_btn():
    accept = InlineKeyboardButton(text="✅ Ma'lumotlarni tasdiqlash", callback_data="accepted")
    cancel = InlineKeyboardButton(text = "🗑 Ma'lumotlarni bekor qilish", callback_data="cancelled")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])
