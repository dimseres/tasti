from django.contrib import admin
from .models import *

admin.site.register(CourseMessage)
admin.site.register(CourseComment)
admin.site.register(CourseTask)
admin.site.register(CourseListener)
admin.site.register(CourseMessageAttachedFile)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'title', 'description', 'slug', 'invitation_link', 'created_at')
    search_fields = ('title', 'description', 'invitation_link')
    fields = ('author_id', 'title', 'description')


@admin.register(CourseMeta)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'cover_image')
    search_fields = ('course_id', 'cover_image')
