from aiogram.fsm.state import StatesGroup, State


class LanguageState(StatesGroup):
    language = State()

class MenuState(StatesGroup):
    menu = State()

class Subscribe(StatesGroup):
    subscribe = State()
class Info(StatesGroup):
    info = State()
class File(StatesGroup):
    file = State()
class Ai(StatesGroup):
    ai = State()

class Messeage(StatesGroup):
    age=State()
    study_level=State()
    current_study=State()
    region=State()
    direction=State()
    education_type=State()
    application_type=State()
    university_priority=State()
    assistance=State()
    source=State()
    extra_number=State()
    passport = State()
    language = State()
    phone = State()
    full_name = State()
    photo = State()
    experience = State()
    degree = State()
    certifications_name = State()
    certifications = State()
    customMessage=State()
    accept=State()
