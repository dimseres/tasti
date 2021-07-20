from django.shortcuts import render
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserInfo


# Create your views here.
class ProfileDetail(RetrieveAPIView):
    queryset = User.objects.all().filter(is_active=True)
    serializer_class = UserInfo
    lookup_url_kwarg = 'username'
    lookup_field = 'username'


class ProfileUpdate(UpdateAPIView):
    queryset = User.objects.all().filter(is_active=True)
    serializer_class = UserInfo
    lookup_url_kwarg = 'username'
    lookup_field = 'username'
