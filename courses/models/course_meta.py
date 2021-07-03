from django.db import models
from .course import Course


class CourseMeta(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    cover_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Доп инфо Курса'
        verbose_name = 'Доп инфо Курса'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.course_id}"
