from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('register/', views.register, name='register'),
    #path('logout/', views.logout, name='logout'),

]
