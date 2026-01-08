from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('scout/', views.scout_dashboard, name='scout'),
    path('leader/', views.leader_dashboard, name='leader'),
    path('', views.home, name='home'),
]