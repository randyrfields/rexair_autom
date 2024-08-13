from django.urls import path
from stations import views

urlpatterns = [
    path("", views.home, name="home"),
]