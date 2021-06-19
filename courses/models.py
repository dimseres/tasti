from django.db import models
from django.contrib.auth.models import User
import short_url
import uuid


class Course(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField()
    invitation_link = models.CharField(default=short_url.encode_url(uuid.uuid4().int))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CourseMeta(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    cover_image = models.ImageField(null=True, blank=True)


class CourseListener(models.Model):
    pass


class CourseMessage(models.Model):
    pass


class CourseTask(models.Model):
    pass