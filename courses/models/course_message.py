from django.db import models
from django.contrib.auth.models import User
from .course import Course


class CourseMessage(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()   # RAW Format must exclude specials chars before publish
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)