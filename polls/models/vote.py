from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField
from accounts.models import User
from .pool import Pool
from .question import Question
from .answer import Answer


class Vote(models.Model):
    pool_id = models.ForeignKey(Pool, on_delete=models.CASCADE, null=False)
    question_id = models.ForeignKey(Question, on_delete=models.PROTECT, null=False)
    answer_id = models.ForeignKey(Answer, on_delete=models.PROTECT, null=False)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Ответы пользователей'
        verbose_name = 'Ответ пользователя'
        ordering = ['-created_at']
