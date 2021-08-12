from _testcapi import raise_exception

from django.core.serializers import serialize
from django.http import JsonResponse
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from ..models import Course, CourseComment, CourseMessage
from ..serializers import CourseAll, CoursePost, CourseDetail
from django.contrib.contenttypes.models import ContentType


