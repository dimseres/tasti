from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField
from .pool import Pool
from .question_category import QuestionCategory


class Question(models.Model):
    TYPE_CHOICE = (
        (1, 'single choice'),       # Только один вариант на выбор
        (2, 'multiply choice'),     # Несколько вариантов на выбор
        (3, 'manual choice'),       # Один вариант на выбор + свой вариант
    )
    pool_id = models.ForeignKey(Pool, on_delete=models.PROTECT, null=False)
    type = models.IntegerField(choices=TYPE_CHOICE, default=1)
    content = models.TextField(null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Вопрос'
        verbose_name = 'Вопросы'
        ordering = ['-created_at']
