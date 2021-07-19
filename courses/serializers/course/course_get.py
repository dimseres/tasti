from rest_framework import serializers
from ...models import *
from django.contrib.auth.models import User


class CourseMeta(serializers.ModelSerializer):
    class Meta:
        model = CourseMeta
        fields = ['cover_image']


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']


class CourseAll(serializers.ModelSerializer):
    # course_meta = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # course_meta = CourseMeta(many=True, read_only=True, allow_null=True)
    course_meta = CourseMeta(source='coursemeta', read_only=True)
    author = UserInfo(source='author_id', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'slug', 'title', 'description', 'created_at', 'course_meta', 'author']
