from django.contrib.auth import views as auth_views

from django.views import generic
from django.urls import reverse_lazy

from .forms import MyUserCreationForm, MyAuthenticationForm
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


class MySignupView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


class MyLoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    form_class = MyAuthenticationForm
    success_url = reverse_lazy('art:index')


class MyPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'users/password-change-form.html'
    success_url = reverse_lazy('users:password-change-done')
    form_class = MyPasswordChangeForm


class MyPasswordResetView(auth_views.PasswordResetView):
    template_name = 'users/password-reset.html'
    success_url = reverse_lazy('users:password-reset-done')
    form_class = MyPasswordResetForm


class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'users/password-reset-confirm.html'
    form_class = MySetPasswordForm

