from django.urls import path
from .views import add

urlpatterns = [
    # path('', CategoryDetail.as_view(), name='category'),
    path('<int:pk>', add),
]