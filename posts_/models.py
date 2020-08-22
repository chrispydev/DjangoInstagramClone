from django.db import models


class Posts(models.Model):
    picture = models.ImageField(upload_to='post_pic')
    content = models.TextField()
