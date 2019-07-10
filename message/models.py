from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Message(models.Model):
    problem_id = models.IntegerField()
    member_id = models.ForeignKey(User, related_name="sender")
    nickname = models.
    reciever = models.ForeignKey()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)