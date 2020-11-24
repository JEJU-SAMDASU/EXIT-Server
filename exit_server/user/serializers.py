from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _
import jwt, copy

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
        fields = ("uid", "email", "password", "name", "is_counselor", "is_client", "introduction", "category", "able_time")

    def create(self, validated_data):
        created_validated_data = copy.deepcopy(validated_data)
        created_validated_data.pop('category')
        created_validated_data.pop('able_time')
        user = User.objects.create(**created_validated_data)

        for j in validated_data["category"]:
            for i in Category.objects.all():
                if i.subject == j:
                    break
            else:
                category = Category.objects.create(subject=j)
                user.category.add(category)

        for i, able_time in enumerate(validated_data['able_time']):
            able_from,able_to = able_time.split("~")
            AbleTime.objects.create(counselor_id = validated_data['uid'],day = i, able_from = able_from, able_to = able_to)

        return user


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uid", "email", "password", "name")

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LoginCounselorSerializer(serializers.Serializer):
    uid = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        credentials = {"uid": data["uid"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            payload = {"uid": user.uid, "email": user.email}

            token = utils.jwt_encode_handler(payload)
            return user, token

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)


class LoginClientSerializer(serializers.Serializer):
    uid = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        credentials = {"uid": data["uid"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            payload = {"uid": user.uid, "email": user.email}

            token = utils.jwt_encode_handler(payload)
            return user, token

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)

class CounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uid", "email", "password", "name", "is_counselor", "is_client", "introduction", "category", "able_time")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uid", "email", "password", "name")