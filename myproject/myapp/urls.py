from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
]
