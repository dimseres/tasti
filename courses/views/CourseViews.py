from _testcapi import raise_exception

from django.core.serializers import serialize
from django.http import JsonResponse
from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from ..models import Course
from ..serializers import CourseAll, CoursePost


class CourseView(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseAll(courses, many=True)
        return Response(serializer.data)


class CourseAPI(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePost
    permission_classes = (IsAuthenticated,)

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