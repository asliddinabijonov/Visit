from django.db import models
from django.contrib.auth.models import AbstractUser

class TurUser(AbstractUser):
    USER_TYPES = [
        ('sayohatchi', 'Sayohatchi'),
        ('taxi_egasi', 'Taxi park egasi'),
        ('gid', 'Gid (yo‘lboschi)'),
        ('mehmonxona_egasi', 'Mehmonxona egasi'),
    ]

    user_type = models.CharField(max_length=30, choices=USER_TYPES, verbose_name="Foydalanuvchi turi")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam", blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name="Davlat", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Shahar", blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Profil rasmi")
    description = models.TextField(blank=True, null=True, verbose_name="Qo‘shimcha ma’lumot")

    def __str__(self):
        return f"{self.username} — {self.get_user_type_display()}"

    class Meta:
        verbose_name = "TurUser"
        verbose_name_plural = "TurUser"
