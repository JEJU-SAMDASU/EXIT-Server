from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CreateCounselorSerializer, CreateClientSerializer, LoginCounselorSerializer, LoginClientSerializer, CounselorSerializer, ClientSerializer


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
    serializer_class = LoginCounselorSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data
        return Response(
            {"user": CounselorSerializer(user).data, "token": token}, status=status.HTTP_200_OK,
        )

class ClientLoginView(generics.GenericAPIView):
    serializer_class = LoginClientSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data
        return Response(
            {"user": ClientSerializer(user).data, "token": token}, status=status.HTTP_200_OK,
        )
