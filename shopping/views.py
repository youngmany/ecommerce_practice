from django.shortcuts import render
from django.http import HttpResponse

from carton.cart import Cart
from product.models import Product

def add(request):
    cart = Cart(request.session)
    print(request.GET.get('product_id'))
    product = Product.objects.get(id=int(request.GET.get('product_id')))
    cart.add(product, price=product.price)
    return HttpResponse("Added")


def show(request):
    return render(request, 'cart_show.html')