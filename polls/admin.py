from django.contrib import admin
from .models import *


@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    list_display = ('creator_id', 'title', 'description', 'short_url', 'status', 'created_at')
    search_fields = ('title', 'status', 'created_at')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pool_id', 'question_id', 'content', 'is_correct', 'created_at')
    search_fields = ('content',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pool_id', 'type', 'content', 'created_at')
    search_fields = ('content',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('pool_id', 'question_id', 'content', 'answer_id', 'user_id')
