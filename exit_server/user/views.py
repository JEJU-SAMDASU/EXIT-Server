from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import (
    CreateCounselorSerializer,
    CreateClientSerializer,
    LoginUserSerializer,
    CounselorSerializer,
    ClientSerializer,
    AbleTimeSerializer,
)
from .models import User, Category, AbleTime
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework.permissions import IsAuthenticated


class CounselorRegisterationView(generics.GenericAPIView):
    serializer_class = CreateCounselorSerializer

    def post(self, request):
        if len(request.data["password"]) < 8:
            message = {"message": "password is too short"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.validated_data

        return Response(user_data, status=status.HTTP_201_CREATED)


class ClientRegisterationView(generics.GenericAPIView):
    serializer_class = CreateClientSerializer

    def post(self, request):
        if len(request.data["password"]) < 8:
            message = {"message": "password is too short"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.validated_data

        return Response(user_data, status=status.HTTP_201_CREATED)


"""
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    return Response(
        {"user": CounselorSerializer(user).data}, status=status.HTTP_201_CREATED
    )
"""


class CounselorLoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    lookup_field = "uid"

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data

        result = CounselorSerializer(user).data
        result["category"] = [c.subject for c in Category.objects.filter(user=user.uid)]
        return Response(
            {"user": result, "token": token},
            status=status.HTTP_200_OK,
        )


class ClientLoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data
        return Response(
            {"user": ClientSerializer(user).data, "token": token},
            status=status.HTTP_200_OK,
        )


class UserView(generics.RetrieveAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = CounselorSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = "uid"

    def get(self, request, *args, **kwargs):
        instance = User.objects.get(uid=request.user.uid)
        serializer = self.get_serializer(instance)
        result = serializer.data
        result["category"] = [
            c.subject for c in Category.objects.filter(user=request.user.uid)
        ]
        return Response(result)


class CounselorListView(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = CounselorSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = "uid"

    def list(self, request):
        queryset = User.objects.filter(is_counselor=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AbleTimeView(generics.RetrieveAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AbleTimeSerializer
    permission_classes = [IsAuthenticated]
    queryset = AbleTime.objects.all()

    def get(self, request, *args, **kwargs):
        if not request.user.is_counselor:
            return Response({"message": "you are not conselor"}, status=401)

        abletimes = AbleTime.objects.filter(counselor=kwargs["uid"])
        result = []
        for abletime in abletimes:
            serializer = self.get_serializer(abletime)
            if serializer.data["is_available"]:
                result.append(serializer.data)
        return Response({"able_times": result})
