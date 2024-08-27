from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']

class UserChange_Form(UserChangeForm):
    password = None 

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 