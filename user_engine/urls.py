from django.urls import path
from user_engine import views

urlpatterns = [
    path("",views.dashboard, name="dashboard")
]
