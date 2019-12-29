from django.shortcuts import render, redirect
from carton.cart import Cart
from product.models import Product


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=int(request.GET.get('product_id')))
    cart.add(product, price=product.price, quantity=int(request.GET.get('test')))
    
    return redirect('/product/' + request.GET.get('product_id'))

# def show(request):
#    return render(request, 'mypage.html')