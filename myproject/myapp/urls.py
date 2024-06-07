from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    #reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    #settings
    path('settings/', views.settings_view, name='settings'),
    path('change-password/', views.change_password, name='change_password'),

]
