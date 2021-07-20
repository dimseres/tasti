from rest_framework import serializers
from ...models import *
from accounts.models import User


class Author(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'first_name', 'last_name']


class CourseMeta(serializers.ModelSerializer):
    class Meta:
        model = CourseMeta
        fields = ['cover_image']


class CourseMessages(serializers.ModelSerializer):
    user = Author(source='authorid', read_only=True)

    class Meta:
        model = CourseMessage
        fields = ['text', 'updated_at', 'user']


class CourseAll(serializers.ModelSerializer):
    # course_meta = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # course_meta = CourseMeta(many=True, read_only=True, allow_null=True)
    course_meta = CourseMeta(source='coursemeta', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'slug', 'title', 'description', 'created_at', 'course_meta', 'author_id']


class CourseDetail(serializers.ModelSerializer):
    course_meta = CourseMeta(source='coursemeta', read_only=True)
    messages = CourseMessages(source='coursemessage_set', read_only=True, many=True)
    author = Author(source='author_id', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'slug', 'title', 'description', 'created_at', 'course_meta', 'author', 'messages']