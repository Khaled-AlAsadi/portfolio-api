from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('auth/get-tokens', views.CustomTokenObtainPairView.as_view(),
         name='obtain-token'),
    path('auth/refresh-token', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('auth/verify-token', TokenVerifyView.as_view(), name='verify_token'),
    path('user', views.get_user, name='get-user'),
    path('user/update', views.update_user, name='update-user'),
    path('portfolio/update', views.update_portfolio, name='update-portfolio'),
    path('portfolio/retrive', views.get_portfolio, name='retrive-portfolio'),
    path('work-experinces', views.get_work_experinces, name='work-experinces'),
    path('work-experinces/create', views.create_work_experince,
         name='create-work-experinces'),
    path('work-experinces/delete/<str:id>', views.delete_work_experince,
         name='delete-work-experince'),
    path('work-experinces/update/<str:id>', views.update_work_experince,
         name='update-work-experince'),
    path('language/retrive', views.get_languages, name='get-languages'),
    path('language/create', views.add_language, name='add-language'),
    path('language/delete/<str:id>', views.delete_language,
         name='delete-language'),
    path('language/update/<str:id>', views.update_language,
         name='update-language'),
    path('educations/retrive', views.get_educations,
         name='retrive-educations'),
    path('educations/create', views.create_education, name='create-education'),
    path('educations/delete/<str:id>', views.delete_education,
         name='delete-education'),
    path('educations/update/<str:id>', views.update_education,
         name='update-education'),

]
