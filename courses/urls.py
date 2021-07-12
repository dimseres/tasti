from django.urls import path, include
from .views import CourseView, CourseAPI

urlpatterns = [
    path('all/', CourseView.as_view()),
    path('create/', CourseAPI.as_view())
]