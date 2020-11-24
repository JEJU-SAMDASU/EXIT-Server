from rest_framework.urls import urlpatterns
from .views import signup
from django.contrib import auth

urlpatterns = [
    auth("/signup", signup()),
]