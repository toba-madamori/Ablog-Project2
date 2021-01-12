
from django.urls import path
from members import views
from .views import UserRegisterView, UserUpdateView, PasswordsChangeView
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name= 'register'),
    path('settings/<int:pk>', UserUpdateView.as_view(), name= 'settings'),
    path('password/', PasswordsChangeView.as_view()),
    
]
