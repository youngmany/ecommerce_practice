from django.urls import path
from .views import RegisterView, login, logout, index

urlpatterns = [
    path('', index),
    path('register', RegisterView.as_view()),
    path('login', login),
    path('logout', logout),
]