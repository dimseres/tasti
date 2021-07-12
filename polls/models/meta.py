from django.db import models
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, TextField, URLField, UUIDField
from django.contrib.auth.models import User
from .pool import Pool
from .question import Question
from .answer import Answer


class Meta(models.Model):
    pass
