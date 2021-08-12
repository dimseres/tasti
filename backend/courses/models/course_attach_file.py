from django.db import models
from accounts.models import User
from .course import Course


class CourseAttachedFile(models.Model):
    file = models.FileField(upload_to='course_attach/')
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_attached_file'
        verbose_name_plural = 'Файлы курса'
        verbose_name = 'Файл курса'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.file}"
