from django.db import models
from django.contrib.auth.models import User
from .course import Course


class CourseListener(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
