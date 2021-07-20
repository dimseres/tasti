from rest_framework import serializers
from ...models import Course, CourseMeta


class CourseMeta(serializers.ModelSerializer):
    class Meta:
        model = CourseMeta
        fields = '__all__'


class CoursePost(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['author_id', 'title', 'description']
        # fields = ('author_id', 'title', 'description')
        # fields = ['author_id', 'title', 'description', 'course_meta']
