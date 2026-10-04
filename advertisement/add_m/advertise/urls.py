from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('register/', views.register_view, name='register'),  # user registration
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),  # dashboard after login
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),

]
