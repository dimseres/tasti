from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(null=True, blank=True,
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=('jpeg', 'jpg', 'png'))],
                                   error_messages={'invalid_extension': 'Этот формат не поддерживается'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass
