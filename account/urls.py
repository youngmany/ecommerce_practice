from django.urls import path
from .views import RegisterView, login, logout


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', login),
    path('logout', logout),
]