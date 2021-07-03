from django.db import models
from .course import Course


class CourseMeta(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    cover_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
