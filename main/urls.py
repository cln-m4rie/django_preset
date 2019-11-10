from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(
        template_name='main/registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
