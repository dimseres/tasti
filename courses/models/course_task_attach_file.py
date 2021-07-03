from django.db import models
from django.contrib.auth.models import User
from .course_task import CourseTask


class CourseTaskAttachedFile(models.Model):
    file = models.FileField()
    task_id = models.ForeignKey(CourseTask, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
