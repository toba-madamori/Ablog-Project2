from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdatesettingsForm, PasswordsChangeForm
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UpdatesettingsForm
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('login')

   
class PasswordsChangeView(PasswordChangeView):
    model = User
    form_class = PasswordsChangeForm
    template_name = 'registration/password.html'
    success_url = reverse_lazy('login')

   
