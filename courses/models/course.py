from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from hashlib import sha1
from base64 import b64encode
import short_url
import uuid


class Course(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, validators=[validators.MaxLengthValidator])
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255,
                            validators=[validators.MaxLengthValidator],
                            unique=True)
    invitation_link = models.CharField(max_length=511,
                                       db_index=True,
                                       unique=True,
                                       validators=[validators.MaxLengthValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course'
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.title}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = short_url.encode_url(uuid.uuid4().int)
            self.invitation_link = sha1(str(uuid.uuid4()).encode('utf-8')).hexdigest()
        return super().save(*args, **kwargs)

    class CustomManager(models.Manager):
        def with_all_data(self):
            return self.get_queryset()
