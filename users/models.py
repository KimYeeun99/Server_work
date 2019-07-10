from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        )
    email = models.EmailField(unique=True, verbose_name='이메일')
    name = models.CharField(max_length=20, verbose_name='이름')
    nickname = models.CharField(max_length=20, verbose_name='닉네임')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    