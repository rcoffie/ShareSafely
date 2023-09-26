from django.urls import path

from user_engine import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login_request/", views.login_request, name="login"),
    path("signup/", views.signup, name="signup"),
]
