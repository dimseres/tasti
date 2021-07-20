from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileDetail, ProfileUpdate

urlpatterns = [
    path('<str:username>/', ProfileDetail.as_view()),
    path('<str:username>/update', ProfileUpdate.as_view()),
]