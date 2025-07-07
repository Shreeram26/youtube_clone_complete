from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)
    views = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    thumbnail = models.URLField()

    def __str__(self):
        return self.title
