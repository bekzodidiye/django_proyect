from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('signup/', SingUpView.as_view(), name='signup'),
     path('password-change/', PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
     path('password-change-done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
     path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset_form.html', email_template_name='accounts/password_reset_email.html'), name='password_reset'),
     path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
     path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
     path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
     
     path('logout/', user_logout, name='logout'),
     path('profile/', user_profile, name='user_profile'),
]