from django.db import models
from django.utils import timezone


class Posts(models.Model):
    picture = models.ImageField(upload_to='post_pic')
    content = models.TextField()


class TemPost(models.Model):
    date_posted = timezone.now
    image = models.ImageField(upload_to='tem_post')
