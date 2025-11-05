from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)  # masalan: "Farg‘ona"
    title = models.TextField()  # viloyat haqida qisqacha ma’lumot
    image = models.ImageField(upload_to='regions/')  # viloyat rasmi

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"
        ordering = ['name']  # alfavit bo‘yicha tartiblash

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=100)  # masalan: "Qo‘qon"
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"
        ordering = ['region', 'name']
        unique_together = ['region', 'name']  # bir viloyatda tuman nomi unikal bo‘lsin

    def __str__(self):
        return f"{self.name} ({self.region.name})"


class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=150)  # masalan: "Qo‘qon Xon saroyi"
    description = models.TextField()

    class Meta:
        verbose_name = "Joy"
        verbose_name_plural = "Joylar"
        ordering = ['district__region__name', 'district__name', 'name']
        unique_together = ['district', 'name']  # bir tumanda joy nomi takrorlanmasin

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/')
    caption = models.CharField(max_length=255, blank=True, null=True)  # rasmga oid tavsif

    class Meta:
        verbose_name = "Joy rasmi"
        verbose_name_plural = "Joy rasmlari"
        ordering = ['place']

    def __str__(self):
        return f"{self.place.name} - Rasm"
