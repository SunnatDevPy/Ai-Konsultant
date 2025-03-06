from django.db import models

class Files_to_download(models.Model):
    caption=models.CharField(max_length=100)
    file=models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.caption



class UniversityApplication(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'O‘zbek'),
        ('ru', 'Rus'),
        ('en', 'Ingliz'),
    ]

    STUDY_MODE_CHOICES = [
        ('day', 'Kunduzgi'),
        ('evening', 'Kechki'),
        ('distance', 'Masofaviy'),
        ('external', 'Sirtqi'),
    ]

    AGE_CHOICES = [
        ('17-19', '17-19'),
        ('20-22', '20-22'),
        ('23-25', '23-25'),
        ('25+', '25+'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('bachelor', 'Bakalavriat'),
        ('master', 'Magistratura'),
    ]

    CURRENT_EDUCATION_CHOICES = [
        ('school', 'Maktab'),
        ('college', 'Litsey/Kollej'),
        ('university', 'Universitet'),
    ]

    FINANCIAL_AID_CHOICES = [
        ('grant', 'Grant'),
        ('contract', 'Kontrakt'),
        ('both', 'Ikkalasiga ham topshiraman'),
    ]

    IMPORTANT_FACTOR_CHOICES = [
        ('location', 'Joylashuv'),
        ('price', 'Kontrakt narxi'),
        ('quality', 'Ta’lim sifati'),
        ('grant', 'Grant imkoniyatlari'),
        ('diploma', 'Xalqaro diplom'),
        ('reputation', 'Universitet obro‘si'),
    ]

    HELP_SOURCE_CHOICES = [
        ('self', 'O‘zim mustaqil qaror qilaman'),
        ('parents', 'Ota-onam'),
        ('teachers', 'Ustozlarim'),
        ('friends', 'Do‘stlarim'),
    ]

    SOURCE_CHOICES = [
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
        ('search', 'Google / Yandex'),
        ('friend', 'Do‘stim tavsiya qildi'),
        ('other', 'Boshqa'),
    ]

    full_name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=25, unique=True)
    phone_number = models.CharField(max_length=30)
    additional_phone_number = models.CharField(max_length=30, blank=True, null=True)
    age = models.CharField(max_length=30, choices=AGE_CHOICES)
    education_level = models.CharField(max_length=30, choices=EDUCATION_LEVEL_CHOICES)
    current_education = models.CharField(max_length=25, choices=CURRENT_EDUCATION_CHOICES)
    region = models.CharField(max_length=100)
    desired_major = models.CharField(max_length=255)
    education_language = models.CharField(max_length=30, choices=LANGUAGE_CHOICES)
    study_mode = models.CharField(max_length=30, choices=STUDY_MODE_CHOICES)
    financial_aid = models.CharField(max_length=30, choices=FINANCIAL_AID_CHOICES)
    important_factor = models.CharField(max_length=30, choices=IMPORTANT_FACTOR_CHOICES)
    help_source = models.CharField(max_length=30, choices=HELP_SOURCE_CHOICES)
    tg_id=models.BigIntegerField(unique=True)
    bot_source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
class TemporaryUser(models.Model):
    interface_language = models.CharField(max_length=10)
    tg_id = models.BigIntegerField()
    def __str__(self):
        return self.name
class StudyDirections_uz(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class StudyDirections_ru(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class ChannelsToSubscribe(models.Model):
    name=models.CharField(max_length=100)
    link=models.CharField(max_length=100)

    def __str__(self):
        return self.link


class Referral(models.Model):
    referrer_id = models.BigIntegerField()
    referred_user_id = models.BigIntegerField()


class AllUsersTgId(models.Model):
    tg_id=models.BigIntegerField()
    referal_count=models.IntegerField(default=0)

    def __str__(self):
        return self.tg_id



