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
    introduction = models.CharField(max_length=255, null=True)
    category = models.ManyToManyField(Category, null=True)


class AbleTime(models.Model):
    counselor = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField()
    able_from = models.CharField(max_length=50)
    able_to = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)