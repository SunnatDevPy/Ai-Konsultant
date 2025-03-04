
from bot.models import ChannelsToSubscribe
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def accept_btn():
    accept = InlineKeyboardButton(text="✅ Ma'lumotlarni tasdiqlash", callback_data="accepted")
    cancel = InlineKeyboardButton(text = "🗑 Ma'lumotlarni bekor qilish", callback_data="cancelled")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])
def accept_btn_ru():
    accept = InlineKeyboardButton(text="✅ Проверка данных", callback_data="accepted")
    cancel = InlineKeyboardButton(text = "🗑 Отмена данных", callback_data="cancelled")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])

def join_chanels():
    channels=ChannelsToSubscribe.objects.all()
    buttons = [InlineKeyboardButton(text=f"Join {channel}", url=f"https://t.me/{channel}") for channel in channels]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])