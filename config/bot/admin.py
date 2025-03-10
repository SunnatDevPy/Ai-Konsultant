from django.contrib import admin
from django.contrib.auth.models import Group, User
from adminsortable2.admin import SortableAdminMixin
from bot.models import (
    UniversityApplication,
    TemporaryUser,
    StudyDirections_uz,
    StudyDirections_ru,
    ChannelsToSubscribe,
    Files_to_download,
)


admin.site.register(TemporaryUser)
admin.site.register(StudyDirections_uz)
admin.site.register(StudyDirections_ru)
admin.site.register(ChannelsToSubscribe)
class ApplicationUniversity(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['full_name', 'phone_number']
    ordering = ('order',)

class FilesToDownloadAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("caption", "file", "order")
    ordering = ("order",)
admin.site.register(UniversityApplication,ApplicationUniversity)
admin.site.register(Files_to_download, FilesToDownloadAdmin)


admin.site.unregister(Group)
admin.site.unregister(User)
