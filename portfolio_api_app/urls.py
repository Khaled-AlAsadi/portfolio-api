from . import views
from django.urls import path, include

urlpatterns = [
    path('auth/obtain-token', views.CustomTokenObtainPairView.as_view(), name='obtain-token'),
    path('user', views.get_user, name='get-user'),
    path('user/update', views.update_user, name='update-user'),
    path('portfolio/update', views.update_portfolio, name='update-portfolio'),
    path('portfolio/retrive', views.get_portfolio, name='retrive-portfolio'),
    path('work-experinces', views.get_work_experinces, name='work-experinces'),
    path('work-experinces/create', views.create_work_experince, name='create-work-experinces'),
    path('work-experinces/delete/<str:id>', views.delete_work_experince, name='delete-work-experince'),
    path('work-experinces/update/<str:id>', views.update_work_experince, name='update-work-experince'),
    path('languages/retrive', views.get_languages, name='get-languages'),
    path('languages/create', views.add_language, name='add-language'),
    path('languages/delete/<str:id>', views.delete_language, name='delete-language'),
    path('languages/update/<str:id>', views.update_language, name='update-language'),

]
