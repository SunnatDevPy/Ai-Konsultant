from tg_bot.language_db import uz, ru
from bot.models import StudyDirections_uz,StudyDirections_ru
boshqa = "✍️ Boshqa"
drugoy ="✍️ Другой"
ortga = "🔙 Ortga"
menuga_uz='🔙 Asosiy menu qaytish'
menuga_ru='🔙 Главное меню'
nazad = "🔙 Назад"
uz_text = "🇺🇿 O'zbek"
ru_text = "🇷🇺 Русский"
commands = [uz.get('servis_btn1'), uz.get('servis_btn2'), ru.get('servis_btn1'), ru.get('servis_btn2')]
File_servis = [uz.get('servis_btn1'), ru.get('servis_btn1')]
univer = ['Bakalavriat', 'Magistratura', 'Бакалавриат', 'Степень магистра']
current = ['Maktab', 'Litsey/Kollej', 'Universitet', 'Школа', 'Средняя школа/колледж', 'Университет']
regions_valid = [
    "Toshkent shahri", "Toshkent viloyati", "Andijon viloyati", "Fargʻona viloyati",
    "Namangan viloyati", "Samarqand viloyati", "Buxoro viloyati", "Xorazm viloyati",
    "Navoiy viloyati", "Qashqadaryo viloyati", "Surxondaryo viloyati",
    "Jizzax viloyati", "Sirdaryo viloyati", "Qoraqalpogʻiston Respublikasi","Город Ташкент", "Ташкентская область", "Андижанская область", "Ферганская область",
    "Наманганская область", "Самаркандская область", "Бухарская область", "Хорезмская область",
    "Навоийская область", "Кашкадарьинская область", "Сурхандарьинская область",
    "Джизакская область", "Сырдарьинская область", "Республика Каракалпакстан",ortga,nazad
]
study_directions1 = list(StudyDirections_uz.objects.values_list("name", flat=True))
study_directions2 = list(StudyDirections_ru.objects.values_list("name", flat=True))
button_texts = [
    "🇺🇿 O‘zbek",
    "🇷🇺 Русский",
    "🇺🇸 English",
    nazad  ,ortga
]

education_buttons = [
    "🏞 Kunduzgi",
    "🌃 Kechki",
    "⛺️ Sirtqi",
    "🛣 Masofaviy",
    ortga,"🏞 Дневное обучение",
    "🌃 Вечернее обучение",
    "⛺️ Заочное обучение",
    "🛣 Удаленное обучение",
    nazad
]

application_btn = [
    "💲 Grant", "🔖 Kontrakt",
    "🧮 Ikkalasiga ham topshiraman", ortga,"🧮 Подам заявку на оба", nazad,"💲 Грант", "🔖 Контракт"
]
all_btn = [
    "📍 Joylashuv",
    "📉 Kontrakt narxi",
    "📖 Ta’lim sifati",
    "💱 Grant imkoniyatlari",
    "🌐 Xalqaro diplom",
    "📌 Universitet obro‘si",
    ortga,
    "📍 Расположение",
    "📉 Цена контракта",
    "📖 Качество образования",
    "💱 Возможности стипендии",
    "🌐 Международный диплом",
    "📌 Репутация университета",
    nazad
]
all_btns = [
    # Uzbek
    "🙍 O‘zim mustaqil qaror qilaman",
    "👨‍👩‍👦‍👦 Ota-onam",
    "👩‍🏫 Ustozlarim",
    "👫 Do‘stlarim",
    ortga,

    # Russian
    "🙍 Я принимаю самостоятельное решение",
    "👨‍👩‍👦‍👦 Мои родители",
    "👩‍🏫 Мои учителя",
    "👫 Мои друзья",
    nazad
]
all_buttons = [
    # Uzbek
    "📸 Instagram",
    "🛫 Telegram",
    "🔎 Google / Yandex",
    "👫 Do‘stim tavsiya qildi",
    "✍️ Boshqa",
   ortga,

    # Russian
    "📸 Инстаграм",
    "🛫 Телеграм",
    "🔎 Google / Яндекс",
    "👫 Мой друг рекомендовал это",
    "✍️ Другое",
    nazad
]





