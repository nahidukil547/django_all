from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view_username_pass, name='login'),
    path("logout/", views.user_logout, name="logout"),
    path("reset-password/", views.reset_pass, name="reset_password"),
    path("change-password/", views.change_pass, name="change_password"),
    path("forgot-password/", views.forgot_pass, name="forgot_password"),
    path('', views.home, name='home'),
]