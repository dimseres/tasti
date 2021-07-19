from rest_framework import serializers
from ...models import Course, CourseMeta


class CourseMeta(serializers.ModelSerializer):
    class Meta:
        model = CourseMeta
        fields = '__all__'


class CoursePost(serializers.ModelSerializer):
    course_meta = CourseMeta(source='course_meta_set', read_only=True)

    class Meta:
        model = Course
        # fields = ('author_id', 'title', 'description')
        fields = ['author_id', 'title', 'description', 'course_meta']

    def create(self, validated_data):
        course = Course.objects.create(**validated_data)
        if 'course_meta' in validated_data:
            course_meta_dict = validated_data['course_meta']
            course_meta_dict['course_id'] = course
            CourseMeta.objects.create(**course_meta_dict)
        return course
