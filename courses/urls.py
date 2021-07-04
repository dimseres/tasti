from django.urls import path, include
from .views import api_courses

urlpatterns = [
    path('all/', api_courses)
]