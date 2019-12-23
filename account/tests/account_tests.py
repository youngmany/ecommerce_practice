import pytest
from django.shortcuts import reverse
from django.contrib.auth.models import User
from account.forms import RegisterForm


#fixture = ?
@pytest.fixture(scope='function')
def access_db(db):
    pass

@pytest.fixture(scope='module')
def create_obj(django_db_blocker):
    with django_db_blocker.unblock():
        obj = User.objects.create(
            username='ymkim3',
            password='123123'
        )

def test_user_register_form():
    form = RegisterForm(
        data={
            'username': 'ymkim1',
            'password': '123123',
            're_password': '123123'
        }
    )

    assert form.is_valid()

def test_registerview_post(client, access_db, create_obj):
    resp = client.post(
        reverse('register'),
        data={
            'username': 'ymkim1',
            'password': '123123',
            're_password': '123123'
        }
    )
    assert resp.status_code == 302
    obj = User.objects.first()
    print(obj.username)
    assert isinstance(obj, User)

"""
def test_loginview_post(client, access_db, create_obj):
    url = reverse('login') 
    resp = client.post(
        url,
        data={
            'username': 'ymkim3',
            'password': '123123',
        }
    )

    assert resp.status_code == 302
"""