from django.contrib import admin
from bot.models import UniversityApplication,TemporaryUser,StudyDirections_uz,ChannelsToSubscribe,StudyDirections_ru


admin.site.register(UniversityApplication)
admin.site.register(TemporaryUser)
admin.site.register(StudyDirections_uz)
admin.site.register(StudyDirections_ru)
admin.site.register(ChannelsToSubscribe)