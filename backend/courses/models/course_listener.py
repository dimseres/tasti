from django.db import models
from accounts.models import User
from .course import Course


class CourseListener(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_listener'
        verbose_name_plural = 'Слушатели курса'
        verbose_name = 'Слушатель курса'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}  {self.course_id}  {self.user_id}"

