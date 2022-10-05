
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django import forms


class MySetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Новый пароль',
        }))
    new_password2 = forms.CharField(
        label='Подтвердите новый пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Подтвердите новый пароль',
        }))


class MyPasswordResetForm(PasswordResetForm):

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={"class": "rounded-0 w-100 input-area name mb-4", 'placeholder': 'Введите e-mail',}))

class MyPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Старый пароль',
        }))
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Новый пароль',
        }))
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Подтвердите пароль',
        }))


class MyUserCreationForm(UserCreationForm):

    username = UsernameField(label='', widget=forms.TextInput(
        attrs={'class': 'rounded-0 w-100 input-area name, mb-4', 
            'placeholder': 'Имя', }))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={"class": "rounded-0 w-100 input-area name mb-4", 'placeholder': 'e-mail',}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Пароль',
        }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'rounded-0 w-100 input-area name mb-4',
            'placeholder': 'Подтвердите пароль',
        }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MyAuthenticationForm(AuthenticationForm):

#    def __init__(self, *args, **kwargs):
#        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
#        self.fields['password'].label = "Пароль"

    username = UsernameField(label='', widget=forms.TextInput(
        attrs={
            'class': 'rounded-0 w-100 input-area name, mb-4', 
            'placeholder': 'Имя',}))

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'rounded-0 w-100 input-area name',
            'placeholder': 'Пароль',
        }))

