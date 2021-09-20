from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('auth/', include('protego.urls')),
    path('courses/', include('courses.urls')),
    path('account/', include('accounts.urls'))
]