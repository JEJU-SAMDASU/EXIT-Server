from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    subject = models.CharField(max_length=50)


class User(AbstractUser):
    uid = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(unique=True, max_length=50)
    username = models.CharField(max_length=50)
    is_counselor = models.BooleanField()
    is_client = models.BooleanField()
    introduction = models.CharField(max_length=255, null=True)
    category = models.ManyToManyField(Category, null=True)

    USERNAME_FIELD = "uid"


class AbleTime(models.Model):
    counselor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="counselor"
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client", null=True)
    day = models.IntegerField()
    able_from = models.CharField(max_length=50)
    able_to = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    concern = models.CharField(max_length=255, null=True)
    is_video = models.BooleanField(default=False)