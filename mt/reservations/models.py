from django.db import models
from django.contrib.auth import get_user_model
from tables.models import Table

User = get_user_model()

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидает"),
        ("confirmed", "Подтверждено"),
        ("canceled", "Отменено"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Бронь {self.user.username} на {self.date} ({self.get_status_display()})"
