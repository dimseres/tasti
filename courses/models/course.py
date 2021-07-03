from django.db import models
from django.contrib.auth.models import User
import short_url
import uuid


class Course(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    invitation_link = models.CharField(max_length=255, default=short_url.encode_url(uuid.uuid4().int), db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.title}"
