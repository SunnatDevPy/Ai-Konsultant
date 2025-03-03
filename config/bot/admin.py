from django.contrib import admin
# from bot.models import User, Certification, Kpi, File, Bonus
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['full_name', 'phone', 'role', 'ball']
#     search_fields = ['full_name', 'phone']
#     list_filter = ["role", 'ball']
#
#
# @admin.register(Certification)
# class CertificationAdmin(admin.ModelAdmin):
#     list_display = ['user__full_name','type','degree','created_at']
#     search_fields = ['user__full_name','type','degree']
#     list_filter = ["type","created_at"]
#
#
# @admin.register(Kpi)
# class KpiAdmin(admin.ModelAdmin):
#     list_display = ['user__full_name','type','ball','created_at']
#     search_fields = ['user__full_name','type','ball']
#     list_filter = ["type","created_at"]
#
#
# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ['file','created_at']
#
#
# @admin.register(Bonus)
# class BonusAdmin(admin.ModelAdmin):
#     list_display = ['user__full_name',"amount",
#                     'type',"comment",'created_at']
#     search_fields = ['user__full_name','type']
#     list_filter = ["type","created_at"]
#
