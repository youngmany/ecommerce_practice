from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, RegisterForm
from product.models import Product


class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            # 'user': request.session.get('user'),
            'product_list': Product.objects.all()
        })


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = User(
            username = form.data.get('username'),
            password=make_password(form.data.get('password')),
        )
        user.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('username')
  
        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del request.session['user']
        request.session.modified = True

    return redirect('/')

def mypage(request):
    return render(request, 'mypage.html')
