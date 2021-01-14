
from django.urls import path
from members import views
from .views import UserRegisterView, UserUpdateView, PasswordsChangeView, UserProfileView, EditProfileView, CreateProfileView
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name= 'register'),
    path('settings/<int:pk>', UserUpdateView.as_view(), name= 'settings'),
    path('password/', PasswordsChangeView.as_view()),
    path('<int:pk>/profile', UserProfileView.as_view(), name= 'profile' ),
    path('<int:pk>/edit_profile', EditProfileView.as_view(), name= 'edit_profile'),
    path('<int:pk>/create_profile', CreateProfileView.as_view(), name= 'create_profile'),

    
]
