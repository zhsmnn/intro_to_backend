from django.contrib import admin
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'is_available')
    list_filter = ('is_available',)
