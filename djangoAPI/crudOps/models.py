import email
from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(help_text='please enter ur email')
    password = models.CharField(max_length=50)
