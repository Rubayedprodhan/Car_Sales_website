from django.shortcuts import render,redirect
from . import forms 

from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.
class RegisterView(FormView):
    template_name='register.html'
    form_class=forms.RegistrationForm
    success_url=reverse_lazy('loging')
    def form_valid(self, form):
        form.save()  
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    


class UserLoginView(LoginView):
    template_name='loging.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_valid(form) 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'loging'
        return context

def user_logout(request):
    logout(request)
    return redirect('loging')



