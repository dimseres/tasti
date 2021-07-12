from django.db import models
from django.contrib.auth.models import User
from .course_task import CourseTask


class CourseTaskComment(models.Model):
    course_id = models.ForeignKey(CourseTask, on_delete=models.PROTECT)
    text = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_task_comment'
        verbose_name_plural = 'Комментарии к заданию'
        verbose_name = 'Комментарий к заданию'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.text[:10]}"
