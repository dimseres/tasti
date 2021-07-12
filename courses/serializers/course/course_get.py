from rest_framework import serializers
from ...models import *


class CourseAll(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'created_at')
