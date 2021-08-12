from rest_framework import serializers
from ...models import *
from accounts.models import User
from django.contrib.contenttypes.models import ContentType
from .course_get import Author


class Comments(serializers.ModelSerializer):
    author = Author(source='user', read_only=True)

    class Meta:
        model = CourseComment
        fields = ['content', 'author']
        # fields = '__all__'

