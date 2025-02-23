from django.db import models

class Thread(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.FileField(upload_to='posts/')
    description = models.TextField()
    author = models.CharField(max_length=255)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
