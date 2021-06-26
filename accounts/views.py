from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUserView(CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('all-tasks')


class UserLoginView(LoginView):
    template_name = 'form.html'


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('login')


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('all-tasks')
