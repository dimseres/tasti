from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'title', 'description', 'invitation_link', 'created_at')
    search_fields = ('title', 'description', 'invitation_link')
