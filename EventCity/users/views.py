from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    """Регистрация пользователей"""
    register_template = 'users/register.html'
    redirect_url = 'home'
    
    form_class = RegisterUserForm
    template_name = register_template
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.redirect_url)


class LoginUser(LoginView):
    """Аутентификация пользователей"""
    login_template = 'users/login.html'
    redirect_url = 'home'
    
    form_class = LoginUserForm
    template_name = login_template
    
    def get_success_url(self):
        return reverse_lazy(self.redirect_url)


def logout_user(request):
    logout(request)
    return redirect('home')
