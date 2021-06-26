from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUserView(CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('all-tasks')

    # auto login after register:
    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
        login(self.request, user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'form.html'


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('login')


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('all-tasks')
