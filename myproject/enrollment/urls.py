from django.urls import path
from . import views
from myapp.views import profile_view  # Import the profile view from myapp

urlpatterns = [
    path('enroll/', views.enrollment, name='enrollment'),
    path('process_enrollment/', views.process_enrollment, name='process_enrollment'),
    path('profile/', profile_view, name='profile'),  # Use the imported profile view

]