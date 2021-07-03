from django.db import models
from django.contrib.auth.models import User
from .course import Course


class CourseMessageComment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
