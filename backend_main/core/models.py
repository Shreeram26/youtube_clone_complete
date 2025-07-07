from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
