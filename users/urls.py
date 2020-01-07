
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import activate_account, activation_complete, signup_done, signup

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_request.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<slug:uidb64>/<slug:token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('activate/<slug:uidb64>/<slug:token>/', activate_account, name='activate'),
    path('signup/', signup, name='signup'),
    path('signup/done/', signup_done, name='signup_done'),
    path('signup/success', activation_complete, name='activation_success'),
]
