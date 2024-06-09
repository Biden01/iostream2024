from django.urls import path, include
from djangoUsers.views import Register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]