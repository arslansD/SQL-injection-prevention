# api/urls.py

from django.urls import path
from api.views import UserView

urlpatterns = [
    path('users/', UserView.as_view()),
]
