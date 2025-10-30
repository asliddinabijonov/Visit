from django.contrib import admin
from .models import TurUser

@admin.register(TurUser)
class TurUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('user_type', 'is_active')