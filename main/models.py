from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to="news_video/")
    thumbnail = models.ImageField(upload_to="news_thumbnail/")
    uploaded_on = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Message(models.Model):
    full_name = models.TextField()
    email = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.full_name