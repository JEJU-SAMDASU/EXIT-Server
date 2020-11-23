from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Category(models.Model):
    subject = models.CharField(max_length=50)


class Counselor(AbstractBaseUser):
    uid = models.CharField(primary_key=True)
    email = models.CharField(unique=True)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=255)
    categorys = models.ManyToManyField(Category)
    able_time = models.CharField(max_length=255, default="")


class Client(AbstractBaseUser):
    uid = models.CharField(primary_key=True)
    email = models.CharField(unique=True)
    name = models.CharField(max_length=50)