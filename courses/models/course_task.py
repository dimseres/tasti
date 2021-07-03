from django.db import models
from django.contrib.auth.models import User
from .course import Course


class CourseTask(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
