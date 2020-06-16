from django.urls import path, include
from rest_framework import routers
from .views import lambda_function


urlpatterns = [
    path('lambda/', lambda_function)
]
