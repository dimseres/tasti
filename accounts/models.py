from django.db import models
from django.contrib.auth.models import User


class AccountProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE),
    name = models.CharField(max_length=63)
    surname = models.CharField(max_length=63, null=True)
    third_name = models.CharField(max_length=63, null=True)
    age = models.IntegerField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'account_profile'
        verbose_name_plural = 'Профиль пользователя'
        verbose_name = 'Профиль пользователя'
        ordering = ['-created_at']
