from tg_bot.utils import remove_at_prefix
from bot.models import ChannelsToSubscribe
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def accept_btn():
    accept = InlineKeyboardButton(text="✅ Ma'lumotlarni tasdiqlash", callback_data="accepted")
    cancel = InlineKeyboardButton(text = "🗑 Ma'lumotlarni bekor qilish", callback_data="cancelled")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])
def accept_btn_ru():
    accept = InlineKeyboardButton(text="✅ Проверка данных", callback_data="accepted")
    cancel = InlineKeyboardButton(text = "🗑 Отмена данных", callback_data="cancelled")
    return InlineKeyboardMarkup(inline_keyboard=[[accept], [cancel]])

def join_channels():
    channels = ChannelsToSubscribe.objects.all()
    buttons = [
        InlineKeyboardButton(
            text=channel.name,
            url=f"https://t.me/{remove_at_prefix(channel.link)}"
        )
        for channel in channels
    ]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])

def referral_btn(user_id):
    ikb = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(text='Referal',
                                 url=f"https://t.me/share/url?url=https://t.me/ricoin_bot?start={user_id}"))
    return ikb.as_markup()