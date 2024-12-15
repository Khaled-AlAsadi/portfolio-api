from . import views
from django.urls import path, include

urlpatterns = [
    path('auth/obtain-token', views.CustomTokenObtainPairView.as_view(), name='obtain-token'),
    path('user', views.get_user, name='get-user'),
]
