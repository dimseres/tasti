from django.db import models
from django.contrib.auth.models import User
from .course import Course


class CourseAttachedFile(models.Model):
    file = models.FileField()
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)