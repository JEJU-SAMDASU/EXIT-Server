from django.shortcuts import render
from rest_framework import generics
from user.serializers import AbleTimeSerializer
from user.models import AbleTime
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response


class CreateReservationView(generics.CreateAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AbleTimeSerializer
    permission_classes = [IsAuthenticated]
    queryset = AbleTime.objects.all()

    def post(self, request, *args, **kwargs):
        if not request.user.is_client:
            return Response({"message": "you are not client"}, status=401)

        # counselor 가 request.data["counselor"] 이면서 day 가 request.data["day"]인 컬럼 가져오고 is_available인지 확인
        print(request.data)
        try:
            ableTime = AbleTime.objects.get(
                counselor=request.data["counselor"],
                day=request.data["day"],
                is_available=True,
            )
        except:
            return Response({"message": "could not find ableTime"}, status=201)

        ableTime.is_available = False
        ableTime.save()
        return Response({"reservation": self.get_serializer(ableTime).data}, status=201)
