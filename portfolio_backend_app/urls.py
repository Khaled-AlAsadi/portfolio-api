from . import views
from django.urls import path, include

urlpatterns = [
    path('health/', views.health_check, name='health-check'),
]