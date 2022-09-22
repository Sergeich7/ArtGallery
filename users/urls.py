
from django.urls import path

from art.views import ClearTextView
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.MySignupView.as_view(), name='signup'),
    path('password-change/', views.MyPasswordChangeView.as_view(), name='password-change'),
    path('password-change-done/', ClearTextView.as_view(template_name='users/password-change-done.html'), name='password-change-done'),

    path('password-reset/', views.MyPasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', ClearTextView.as_view(template_name='users/password-reset-done.html'), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', ClearTextView.as_view(template_name='users/password-reset-complete.html'), name='password-reset-complete'),
]
