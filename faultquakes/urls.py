from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='faultquakes-home'),
    path('about/', views.about, name='faultquakes-about'),
]