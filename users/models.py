from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pro_pic')
    name = models.CharField(max_length=200)
    website = models.URLField()
    bio = models.TextField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)

    def __str__(self):
        return f'{self.user.username} Profile'
