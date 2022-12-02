from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .forms import UserLoginForm, PasswordResetForm, PasswordResetConfirmForm


app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'account/registration/login.html',
        form_class = UserLoginForm),
         name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/account/login/'), name = 'logout'),
    path('register/', views.account_register, name = 'register'),
    # path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_account, name = 'edit_account'),
    path('profile/delete_profile/', views.delete_profile, name = 'delete_profile'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="account/user/delete_confirm.html"), name='delete_confirmation'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="account/user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='account/user/password_reset_email.html',
                                                                 form_class=PasswordResetForm), name='password_reset'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                                                                success_url='/account/password_reset_complete/', 
                                                                                                form_class=PasswordResetConfirmForm), name = 'password_reset_confirm'),

    path('password_reset/password_reset_email_confirm/', TemplateView.as_view(template_name="account/user/reset_status.html"),
                                                                                name='password_reset_done'),

    path('password_reset_complete/', TemplateView.as_view(template_name="account/user/reset_status.html"),
                                                            name='password_reset_complete'),

    path('wishlist/add_to_wishlist/<int:id>', views.add_wishlist, name = 'user_wishlist'),
    path('wishlist', views.wishlist, name = 'wishlist')

    
]
