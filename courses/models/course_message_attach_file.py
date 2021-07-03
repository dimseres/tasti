from django.db import models
from django.contrib.auth.models import User
from .course_message import CourseMessage


class CourseMessageAttachedFile(models.Model):
    file = models.FileField()
    message_id = models.ForeignKey(CourseMessage, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
