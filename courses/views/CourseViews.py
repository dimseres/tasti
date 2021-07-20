from _testcapi import raise_exception

from django.core.serializers import serialize
from django.http import JsonResponse
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from ..models import Course
from ..serializers import CourseAll, CoursePost, CourseDetail


class CourseView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseAll


class CourseDetail(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetail
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class CourseAPI(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePost
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': True,
            'message': 'course was created',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)