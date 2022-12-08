from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Theme', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
    message = forms.CharField(label="Text", widget=forms.Textarea(
        attrs={"class":"form-control", "rows": 5}))
    captcha = CaptchaField()


class User_loginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text='Max length 150', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
    first_name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    last_name = forms.CharField(label='Surname', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')




class Newsform(forms.ModelForm):
    # title = forms.CharField(max_length=150,label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label="Text",required=False, widget=forms.Textarea(attrs={"class":"form-control", "rows": 5}))
    # is_published = forms.BooleanField(label="Published?", initial=True)
    # category = forms.ModelChoiceField(empty_label="choose Category", widget=forms.Select(attrs={"class": "form-control"}), queryset=Category.objects.all())
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            if re.search(r'\W', title):
                raise ValidationError('Name cant start with number!')
        return title