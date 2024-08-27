from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
# Create your views here.

from .models import Car,Order,Brand
from . import forms
from . import models
from django.views.generic.edit import UpdateView

@login_required
def profile_view(request):
    user=request.user
    data=Car.objects.filter(author=user)
    oders=Order.objects.filter(user=user)

    context ={
        'data' :data,
        'user' :user,
        'oders': oders


    }
    return render(request,'profile.html',context)

@login_required
def car_details(request, id):
    car = get_object_or_404(Car, id=id)
    comments = car.comments.all()
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = car
            comment.save()
            return redirect('car_detail', id=id)
    else:
        comment_form = forms.CommentForm()
    
    context = {
        'car': car,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'car_detail.html', context)

# @login_required
# def car_buy(requset,id):
#     car= get_object_or_404(Car, id=id)
#     if car.quantity>0:
#         car.quantity -=1
#         car.save()
#         Order.objects.create(user=requset.user,car=car)
#         return redirect('profile')
#     return redirect('car_detail', id=id)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})


@login_required
def car_buy(request, id):
    car = get_object_or_404(Car, id=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car=car)
        return redirect('profile')
    return redirect('car_detail', id=id)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.UserChange_Form
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile Update Successfully')
        return super().form_valid(form)  
     
class PassChangeView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'pass_change.html'
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)

