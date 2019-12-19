from django.test import TestCase
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm


class UserModelTest(TestCase):

    def setUp(self):
        self.first_user = User(
            username='testuser1',
            email='test1@test.com',
            password='123123'
        )
        self.first_user.save()

        self.second_user = User(
            username='testuser2',
            email='test2@test.com',
            password='123123'
        )
        self.second_user.save()

        self.t_user = {
            'email':'t@t123.com',
            'password':123123,
            're_password':123123
        }

    def test_create_user(self):
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 2)

        first_saved_item = saved_users[0]
        second_saved_item = saved_users[1]

        self.assertEqual(self.first_user.email, 'test1@test.com')
        self.assertEqual(self.second_user.email, 'test2@test.com')
    
    def test_user_forms(self):
        form = RegisterForm(
            self.t_user
        )
        # self.assertTrue(form.is_valid())