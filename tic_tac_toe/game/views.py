from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import SignUpForm, LoginForm



class SignUpView(SuccessMessageMixin, FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'
    success_message = "Your account has been created successfully. You are now logged in."


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class LoginView(SuccessMessageMixin, FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    success_message = "You have been logged in successfully."


    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
class SignoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = "You have been logged out in successfully."


class HomeView(TemplateView):
    template_name = 'home.html'