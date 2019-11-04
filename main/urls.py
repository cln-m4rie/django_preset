from django.urls import path

from . import views

urlpatterns = [
    path('', views.SignupView.as_view()),
]