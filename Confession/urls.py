from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('myconfessions', views.myconfessions, name='myconfessions'),
    path('feedback', views.feedback, name='feedback'),
]
