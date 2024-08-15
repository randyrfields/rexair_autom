from django.urls import include, path
from showstations import views

urlpatterns = [
    path( "", views.index, name="index"),
]