from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.db import transaction
from product.models import Product
from .models import Order
from .forms import OrderForm


class OrderView(FormView):
    form_class = OrderForm
    success_url = '/'

    def form_valid(self, form):
        try:
            with transaction.atomic():
                prod = Product.objects.get(pk=form.data.get('product'))
                order = Order(
                    quantity=form.data.get('quantity'),
                    product=prod,
                    user=User.objects.get(username=self.request.session.get('user'))
                )
                order.save()
                prod.stock -= int(form.data.get('quantity'))
                prod.save()
        except User.DoesNotExist:
            return redirect('/account/login')

        return super().form_valid(form)
    
    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
