from django.urls import path
from .views import ProductDetail, CategoryDetail

urlpatterns = [
    path('', CategoryDetail.as_view(), name='category'),
    path('<int:pk>', ProductDetail.as_view()),
]