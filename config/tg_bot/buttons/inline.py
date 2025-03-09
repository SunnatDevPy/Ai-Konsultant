from tg_bot.utils import remove_at_prefix
from bot.models import ChannelsToSubscribe,Files_to_download
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from django.core.paginator import Paginator
from tg_bot.buttons.text import *

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
        [InlineKeyboardButton(
            text=channel.name,
            url=f"https://t.me/{remove_at_prefix(channel.link)}"
        )] for channel in channels
    ]

    buttons.append([InlineKeyboardButton(
        text="✅ Check",
        callback_data="check_subscription"
    )])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def referral_btn(user_id):
    bot_link = f"https://t.me/ricoin_bot?start={user_id}"
    text = "🚀 Bizga qo'shiling va kelajagingiz sari yana bir ulkan qadamni tashlang!"

    ikb = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(
        text='Invite Friends',
        url=f"https://t.me/share/url?url={bot_link}&text={text}"
    ))

    return ikb.as_markup()







def generate_pdf_list_message(page: int = 1, per_page: int = 10):
    pdfs = Files_to_download.objects.all().order_by('-created_at')
    paginator = Paginator(pdfs, per_page)
    page_obj = paginator.get_page(page)

    message_text = f"📄 *DTM test*             (Page {page}/{paginator.num_pages})      \n\n"
    buttons = []

    for index, file in enumerate(page_obj, start=1 + (page - 1) * per_page):
        message_text += f"{index}. {file.caption}\n"
        buttons.append(InlineKeyboardButton(text=str(index), callback_data=f"pdf_{file.id}"))


    keyboard_buttons = [buttons[i:i+5] for i in range(0, len(buttons), 5)]


    navigation_buttons = []
    if page > 1:
        navigation_buttons.append(InlineKeyboardButton(text="⬅️ Prev", callback_data=f"page_{page - 1}"))
    if page < paginator.num_pages:
        navigation_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"page_{page + 1}"))

    if navigation_buttons:
        keyboard_buttons.append(navigation_buttons)

    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return message_text, keyboard

def edit_info_uz():
    keyboard1=InlineKeyboardButton(text="📝 Malumotlarni tahrirlash.",callback_data="edit_info")
    design=[[keyboard1]]
    return InlineKeyboardMarkup(inline_keyboard=design)

def edit_info_ru():
    keyboard1=InlineKeyboardButton(text="📝 Редактировать информацию.",callback_data="edit_info")
    design=[[keyboard1]]
    return InlineKeyboardMarkup(inline_keyboard=design)

