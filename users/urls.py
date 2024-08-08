from django.urls import path
from . import views
from .views import signup_view
from django.contrib.auth import views as auth_views
urlpatterns = [

  path('', views.home, name = "home"),
  path("signup/", signup_view, name="signup"),
  path('logout/', auth_views.LogoutView.as_view(), name="logout"),
  
]