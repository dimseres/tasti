from django.db import models
from django.contrib.auth.models import User
from .course_task import CourseTask


class CourseTaskAttachedFile(models.Model):
    file = models.FileField(upload_to='course_task_attach/')
    task_id = models.ForeignKey(CourseTask, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Прикрепленные файлы задания'
        verbose_name = 'Прикрепленный файл задания'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.file}"
