from django.db import models
from django.contrib.auth.models import User
from .course import Course
from polls.models import Pool


class CourseTask(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    bound_pool = models.ForeignKey(Pool, null=True, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_task'
        verbose_name_plural = 'Задания курса'
        verbose_name = 'Задание курса'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.title}"
