from . import views
from django.urls import path
from .views import signup_redirect

urlpatterns = [
    path('', views.home, name='home'),
    path("signup/redirect/", signup_redirect, name="signup_redirect"),
]