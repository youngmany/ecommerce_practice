import pytest
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm


@pytest.mark.django_db
def test_user_create():
    obj = User.objects.create(
        username='ymkim1',
        password=123123
    )
    assert obj

    obj.save()

def test_user_register_form():
    form = RegisterForm(
        data={
            'username': 'ymkim1',
            'password': 123123,
            're_password': 123123,
        }
    )

    assert form.is_valid()

@pytest.mark.django_db
def test_user_login_form():
    form = LoginForm(
        data={
            'username': 'ymkim1',
            'password': 123123,
        }
    )

    assert form.is_valid()