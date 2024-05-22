from django.urls import path
from . import views
#from myapp.views import profile_view

urlpatterns = [
    path('benefits/', views.benefits_view, name='benefits')
]