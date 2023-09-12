from django.urls import path
from file_engine import views 

urlpatterns = [
    path('',views.Home, name='home')
]
