from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CreateClientSerializer
from .models import Client, Counselor


class ClientRegistrationView(generics.GenericAPIView):
    serializer_class = CreateClientSerializer

    def post(self):
