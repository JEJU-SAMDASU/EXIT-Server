from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _
import jwt, copy
from django.contrib.auth.hashers import make_password

from .models import User, Category, AbleTime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CreateCounselorSerializer(serializers.ModelSerializer):
    category = serializers.ListField()
    able_time = serializers.ListField()

    class Meta:
        model = User
        fields = (
            "uid",
            "email",
            "password",
            "username",
            "is_counselor",
            "is_client",
            "introduction",
            "category",
            "able_time",
        )

    def create(self, validated_data):
        created_validated_data = copy.deepcopy(validated_data)
        created_validated_data.pop("category")
        created_validated_data.pop("able_time")

        created_validated_data["password"] = make_password(
            created_validated_data["password"]
        )
        user = User.objects.create(**created_validated_data)

        for j in validated_data["category"]:
            category = None
            for i in Category.objects.all():
                if i.subject == j:
                    break
            else:
                category = Category.objects.create(subject=j)
            category = category or Category.objects.get(subject=j)
            user.category.add(category)

        for i, able_time in enumerate(validated_data["able_time"]):
            able_from, able_to = able_time.split("~")
            AbleTime.objects.create(
                counselor_id=validated_data["uid"],
                day=i,
                able_from=able_from,
                able_to=able_to,
            )

        return user


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uid", "email", "password", "username")

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)
        return user


class LoginUserSerializer(serializers.Serializer):
    uid = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(data)

        payload = {"uid": user.uid, "email": user.email, "username": user.username}

        token = utils.jwt_encode_handler(payload)
        return user, token


class CounselorSerializer(serializers.Serializer):
    uid = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    is_counselor = serializers.BooleanField()
    is_client = serializers.BooleanField()
    introduction = serializers.CharField()
    category = serializers.CharField()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uid", "email", "password", "username")


class AbleTimeSerializer(serializers.Serializer):
    counselor = serializers.CharField()
    client = serializers.CharField()
    day = serializers.CharField()
    able_from = serializers.CharField()
    able_to = serializers.CharField()
    is_available = serializers.CharField()
    concern = serializers.CharField()
    is_video = serializers.BooleanField()