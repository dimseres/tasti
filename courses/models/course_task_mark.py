from django.db import models
from accounts.models import User
from .course_task import CourseTask


class CourseTaskMark(models.Model):
    task_id = models.ForeignKey(CourseTask, on_delete=models.PROTECT)
    student_id = models.ForeignKey(User, on_delete=models.PROTECT)
    mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_task_mark'
        verbose_name_plural = 'Оценки к заданию'
        verbose_name = 'Оценка задания'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}  {self.task_id} mark: {self.mark}"
