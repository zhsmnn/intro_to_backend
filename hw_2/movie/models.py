from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    producer = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.title