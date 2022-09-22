from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views

from django.views import generic
from django.urls import reverse_lazy

from art.views import AddContextMixin
from .forms import MyUserCreationForm


class MySignupView(AddContextMixin, generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context)


class MyLoginView(AddContextMixin, auth_views.LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('art:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context)


class MyPasswordChangeView(AddContextMixin, auth_views.PasswordChangeView):
    template_name = 'users/password-change-form.html'
    success_url = reverse_lazy('users:password-change-done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context)


class MyPasswordResetView(AddContextMixin, auth_views.PasswordResetView):
    template_name = 'users/password-reset.html'
    success_url = reverse_lazy('users:password-reset-done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context, active_cat='login')


class MyPasswordResetConfirmView(AddContextMixin, auth_views.PasswordResetConfirmView):
    template_name = 'users/password-reset-confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context, active_cat='login')
