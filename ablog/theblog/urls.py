
from django.urls import path
from theblog import views

urlpatterns = [
    path('', views.Home, name= 'home'),
]
