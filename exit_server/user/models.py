from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    subject = models.CharField(max_length=50)

    
class UserManager(BaseUserManager):  # Helper Class
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **kwargs):
        user = self.create_user(
            email,
            password=password,
            username=username,
            **kwargs,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(uid=username)


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
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client", null=True
    )
    day = models.IntegerField(null=True)
    able_from = models.CharField(max_length=50, null=True)
    able_to = models.CharField(max_length=50, null=True)
    is_available = models.BooleanField(default=True)
    concern = models.CharField(max_length=255, null=True)
    is_video = models.BooleanField(default=False)