from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField
from .pool import Pool
from .question import Question


class Answer(models.Model):
    pool_id = models.ForeignKey(Pool, on_delete=models.PROTECT, null=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    content = models.TextField(null=True)
    active = models.BooleanField(default=True)
    is_correct = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Варианты ответов'
        verbose_name = 'Вариант ответа'
        ordering = ['-created_at']