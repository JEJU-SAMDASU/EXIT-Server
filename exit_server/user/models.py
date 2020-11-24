from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Category(models.Model):
    subject = models.CharField(max_length=50)


class User(AbstractBaseUser):
    uid = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    is_counselor = models.BooleanField()
    is_client = models.BooleanField()
    introduction = models.CharField(max_length=255)
    tag = models.ManyToManyField(Category)
    able_time = models.CharField(max_length=255, default="")

