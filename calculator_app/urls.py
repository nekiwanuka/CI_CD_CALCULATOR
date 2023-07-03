# This code is defining the URL patterns for a Django application.
from django.urls import path
from . import views

urlpatterns = [
    path("", views.calculator, name="calculator"),
]
