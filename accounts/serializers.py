from rest_framework import serializers
from .models import User


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        include = '__all__'
        exclude = ('password', 'groups', 'user_permissions', 'is_staff')
        # extra_kwargs = {'url': {'lookup_field': 'username'}}