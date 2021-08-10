from django.urls import path, include
from .views import (
    CourseView,
    CourseAPI,
    CourseDetail,
    MessageComments
)

urlpatterns = [
    path('all/', CourseView.as_view()),
    path('create/', CourseAPI.as_view()),
    # path('messages/<int:course_id>/')
    path('comments/<int:message_id>/', MessageComments.as_view()),
    path('<slug:slug>/', CourseDetail.as_view())
    # path('course/<slug:slug>/update', )
    # path('course/<slug:slug>/meta', )         # update meta
    # path('message/<int:course_id>/all/', )    # view with comment limit 5 and fetch comments
    # path('comments/<int:content_type>/<int:object_id>/', )
    # path('tasks/<int:course_id>/', )
    # path('listeners/<int:course_id>/', )
]
