from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# from .models import Certification, Kpi, Bonus
#
# # Track status change before saving
# @receiver(pre_save, sender=Certification)
# def check_status_change(sender, instance: Certification, **kwargs):
#     if instance.pk:
#         previous = Certification.objects.get(pk=instance.pk)
#         if previous.status != "ACCEPTED" and instance.status == "ACCEPTED":
#             instance._status_changed = True
#
# @receiver(post_save, sender=Certification)
# def on_certificate_create(sender, instance: Certification, created, **kwargs):
#     if not hasattr(instance, "_status_changed"):
#         return
#
#     print("Certification Accepted:", instance.status)
#
#     kpi_points = 0
#     if instance.degree in ["B1", "B2"] and instance.owner == "Student":
#         kpi_points = 10
#     elif instance.degree in ["B1", "B2"] and instance.owner == "ME":
#         kpi_points = 50
#     elif instance.degree in ["C1", "C2"] and instance.owner == "Student":
#         kpi_points = 50
#
#     if kpi_points:
#         Kpi.objects.create(user=instance.user, type="A'lo", ball=kpi_points)
#         instance.user.ball += kpi_points
#         instance.user.save()
#
# @receiver(post_save, sender=Bonus)
# def on_bonus_create(sender, instance: Bonus, created, **kwargs):
#     if created:
#         instance.user.bonus = int(instance.user.bonus or 0) + int(instance.amount or 0)
#         instance.user.save()
#
# @receiver(post_save, sender=Kpi)
# def on_kpi_update(sender, instance: Kpi, created, **kwargs):
#     if created:
#         instance.user.ball = int(instance.user.ball or 0) + int(instance.ball or 0)
#         instance.user.save()
