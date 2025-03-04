from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'table__number')
