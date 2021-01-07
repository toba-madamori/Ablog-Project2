
from django.urls import path
from members import views
from .views import UserRegisterView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name= 'register'),
    
]
