from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _
import jwt

from .models import Counselor, Client


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("uid", "email", "password", "name")

    def  create(self, validated_data):
        return Client.objects.create()



