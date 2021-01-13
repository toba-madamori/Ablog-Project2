from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdatesettingsForm, PasswordsChangeForm
from theblog.models import Profile
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

   
class UserProfileView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context