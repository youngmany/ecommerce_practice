from django.urls import path
from .views import add, show

urlpatterns = [
    # path('', CategoryDetail.as_view(), name='category'),
    path('add', add, name='shopping_add'),
    path('show', show)
]