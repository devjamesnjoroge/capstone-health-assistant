from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/register/', views.register),
    path('auth/login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
    path('profile/', views.profile),
    path('dashboard/', views.dashboard),
    path('history/', views.history),
    path('diet/', views.diet),
    path('posts/', views.posts),
    path('profile/new/', views.create_profile),
    path('medical_history/new/', views.create_medical_history),
    path('diet/new/', views.create_diet),
    path('posts/new/', views.create_post),
]