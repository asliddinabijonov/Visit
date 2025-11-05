from django.contrib import admin
from .models import Region, District, Place, PlaceImage


# --- Inline tahrir uchun: joyga oid rasmlar ---
class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1   # yangi joy qo‘shishda bitta bo‘sh forma
    fields = ('image', 'caption')  # faqat kerakli maydonlar


# --- Joy (Place) admin paneli ---
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'short_description')
    list_filter = ('district__region', 'district')
    search_fields = ('name', 'description')
    inlines = [PlaceImageInline]  # joy ichida rasmlarni kiritish
    ordering = ('district__region__name', 'district__name', 'name')

    def short_description(self, obj):
        return (obj.description[:70] + "...") if len(obj.description) > 70 else obj.description
    short_description.short_description = "Tavsif"


# --- District (Tuman) admin paneli ---
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'short_description')
    list_filter = ('region',)
    search_fields = ('name', 'description')
    ordering = ('region__name', 'name')

    def short_description(self, obj):
        if obj.description:
            return (obj.description[:70] + "...") if len(obj.description) > 70 else obj.description
        return "-"
    short_description.short_description = "Tavsif"


# --- Region (Viloyat) admin paneli ---
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_title')
    search_fields = ('name', 'title')
    ordering = ('name',)

    def short_title(self, obj):
        return (obj.title[:70] + "...") if len(obj.title) > 70 else obj.title
    short_title.short_description = "Qisqacha ma’lumot"

