import string
import random
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, RegisterForm


def index(request):
    return render(request, 'index.html', { 'email': request.session.get('user') })


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'
    # success_url = 'account' # /account/account
    # success_url = '/' # /


    def form_valid(self, form):
        # 유효성 검사 종료 시 호출 함수
        user = User(
            # username으로 변경하거나, AbstractUser 상속하여 따로 정의 OR onetoone으로 계정 내용을 더 추가하여 모델링
            username = random.choice(string.ascii_uppercase),
            email = form.data.get('email'),
            password=make_password(form.data.get('password')),
        )
        user.save()

        return super().form_valid(form)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.data.get('email')
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form })


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')