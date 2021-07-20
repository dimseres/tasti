from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField
from accounts.models import User
from datetime import datetime
import uuid
from hashlib import md5


class Pool(models.Model):
    STATUS_CHOICES = (
        (1, 'Published'),   # Опубликован
        (2, 'Draft'),       # Редактируется
        (3, 'Hidden')       # Скрыт
    )
    TYPE_CHOICE = (
        (1, 'Pool'),    # Тест
        (2, 'Survey')   # Опрос
    )
    # is_time_limited поле для флага ограничения тестирования по времени
    creator_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    title = CharField(max_length=255, db_index=True)
    description = models.TextField(null=True)
    content = models.TextField(null=True)
    uuid = UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    short_url = CharField(max_length=11, unique=True, db_index=True, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2, db_index=True)
    attempts_count = models.IntegerField(default=2)    # Кол-во попыток
    shuffle_question = models.BooleanField(default=False)       # Разный порядок вопросов?
    type = models.IntegerField(choices=TYPE_CHOICE, db_index=True)
    is_time_limited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, null=True)

    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.title}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.short_url = md5(f"{str(self.uuid) + self.title}".encode()).hexdigest()[:10]
        return super().save(*args, **kwargs)
