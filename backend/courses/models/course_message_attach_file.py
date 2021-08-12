from django.db import models
from accounts.models import User
from .course_message import CourseMessage


class CourseMessageAttachedFile(models.Model):
    file = models.FileField(upload_to='course_message_attach/')
    message_id = models.ForeignKey(CourseMessage, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_message_attached_file'
        verbose_name_plural = 'Прикрепленные файлы сообщений'
        verbose_name = 'Прикрепленный файл сообщения'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.file}"
