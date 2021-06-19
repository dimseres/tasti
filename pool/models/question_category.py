from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField


class QuestionCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Категории вопросов'
        verbose_name = 'Категория вопроса'
        ordering = ['-created_at']