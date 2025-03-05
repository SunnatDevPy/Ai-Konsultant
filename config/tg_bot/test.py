import asyncio
import re

import gspread
from aiogram import Bot
from aiogram.enums import ChatMemberStatus
from aiogram.types import ChatMember
from decouple import config
from oauth2client.service_account import ServiceAccountCredentials
from openai import AsyncOpenAI

# from dispatcher import TOKEN

file_place = config("FILE_PLACE")
bot = Bot(token='7888133190:AAEo-uhbITqVDpKi_RBerurbXj9IHQR7-A0')


def format_phone_number(phone_number: str) -> str | bool:
    phone_number = ''.join(c for c in phone_number if c.isdigit())

    # Prepend +998 if missing
    if phone_number.startswith('998'):
        phone_number = '+' + phone_number
    elif not phone_number.startswith('+998'):
        phone_number = '+998' + phone_number

    # Check final phone number length
    if len(phone_number) == 13:
        return phone_number
    else:
        return False


def passport_number_checker(passport_number: str) -> bool:
    return bool(re.fullmatch(r"^[A-Z]{2}\d{7}$", passport_number))


def is_valid_full_name(full_name: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ' -]+", full_name))


async def check_user_subscription(user_id: int, chat_ids: str) -> bool:
    results = {}

    for chat_id in chat_ids:
        try:
            chat_member: ChatMember = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
            subscribed_statuses = {ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR}
            results[chat_id] = chat_member.status in subscribed_statuses
        except Exception as e:
            print(f"❌ Error checking {chat_id}: {e}")
            results[chat_id] = False

    return results


def remove_at_prefix(text: str) -> str:
    return text.lstrip('@')


def save_to_google_sheets(full_name,
                          passport_number,
                          phone_number,
                          additional_phone_number,
                          age,
                          education_level,
                          current_education,
                          region,
                          desired_major,
                          education_language,
                          study_mode,
                          financial_aid,
                          important_factor,
                          help_source,
                          tg_id,
                          bot_source):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(filename=file_place)
    client = gspread.authorize(creds)

    # Open the sheet
    sheet = client.open("University Users Data").sheet1

    sheet.append_row([full_name, passport_number,
                      phone_number,
                      additional_phone_number,
                      age,
                      education_level,
                      current_education,
                      region,
                      desired_major,
                      education_language,
                      study_mode,
                      financial_aid,
                      important_factor,
                      help_source,
                      tg_id,
                      bot_source])




async def ask_AI():
    client = AsyncOpenAI(
        api_key=""
    )

    completion = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Write a haiku about AI"}]
    )

    print(completion.choices[0].message.content)


asyncio.run(ask_AI())
