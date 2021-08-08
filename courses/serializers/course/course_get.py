from rest_framework import serializers
from ...models import *
from accounts.models import User
from django.contrib.contenttypes.models import ContentType


class Author(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'first_name', 'last_name']


class MessageFiles(serializers.ModelSerializer):
    class Meta:
        model = CourseMessageAttachedFile
        fields = ['file', 'updated_at']


class CourseMeta(serializers.ModelSerializer):
    class Meta:
        model = CourseMeta
        fields = ['cover_image']


class LimitedListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.all()[:3]
        return super(LimitedListSerializer, self).to_representation(data)


class Comments(serializers.ModelSerializer):
    author = Author(source='user', read_only=True)

    class Meta:
        model = CourseComment
        fields = ['content', 'author']
        # fields = '__all__'

    def get_fields(self):
        fields = super(Comments, self).get_fields()
        return fields

class MessageComments(serializers.RelatedField):
    def to_representation(self, value):
        ct = ContentType.objects.get_for_model(value)
        serializer = Comments(value, read_only=True, source='last_comments')
        return serializer.data


class CourseMessages(serializers.ModelSerializer):
    user = Author(source='authorid', read_only=True)
    files = MessageFiles(source='coursemessageattachedfile_set', many=True)
    # message_count = serializers.IntegerField(source='comments', read_only=True)

    # def get_message_count(self, obj):
    #     return obj.comments.
    message_comments = MessageComments(queryset='comments', source='comments', many=True)

    class Meta:
        model = CourseMessage
        fields = ['text', 'updated_at', 'user', 'files', 'message_comments']
        # fields = ['text', 'updated_at', 'user', 'files', 'message_count']

class CourseAll(serializers.ModelSerializer):
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
