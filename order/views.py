from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from product.models import Product
from .models import Order
from .forms import OrderForm


class OrderView(FormView):
    form_class = OrderForm
    success_url = '/'

    def form_valid(self, form):
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

        return super().form_valid(form)
    
    # 실패 시
    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    # 폼을 생성해서 어떤 인자값을 전달해서 만들건지
    def get_form_kwargs(self, **kwargs):
        #기존에 슈퍼 호출
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
