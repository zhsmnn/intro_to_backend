from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    title = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.FileField(upload_to='posts/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

