from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField
from .pool import Pool
from .question import Question
from .answer import Answer


class CorrectAnswer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    answer_id = models.ForeignKey(Answer, on_delete=models.PROTECT, null=False)
    is_correct = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Правильные Ответы'
        verbose_name = 'Правильный ответ'
        ordering = ['-created_at']
