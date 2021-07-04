from django.http import JsonResponse
from django.http.request import HttpRequest
from .models import Course
from .serializers import CourseSerializer


def api_courses(request: HttpRequest):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
