from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer,Usuario
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer