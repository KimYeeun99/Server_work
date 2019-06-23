from django.db import models
from users.models import CustomerUser
# Create your models here.

class PostUser(models.Model):
    author = models.ForeignKey(CustomerUser, on_delete = 'CASCADE')
    message = models.CharField(max_length=255)
    