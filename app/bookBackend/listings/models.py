from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=75,primary_key=True)


class Books(models.Model):
    owner = models.ForeignKey(User,
                              related_name='books',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.BooleanField(default=True)
