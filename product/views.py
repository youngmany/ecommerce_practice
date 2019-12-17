from django.shortcuts import render
from django.views.generic import ListView, DetailView
from carton.cart import Cart
from .models import Product, Category


# TODO : 썸네일 이미지
class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CategoryDetail(ListView):
    template_name = 'category_detail.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        # category = Category.objects.get(name=self.request.GET.get('category',''))
        # t = Product.objects.filter(category=category.id) 
        qs = Product.objects.select_related('category').filter(
            category__name=self.request.GET.get('category',''))
        
        return qs