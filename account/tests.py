from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.first_user = User(
            username='testuser1',
            password='123123'
        )
        self.first_user.save()

        self.second_user = User(
            username='testuser2',
            password='123123'
        )
        self.second_user.save()

    def test_create_user(self):
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 2)

        first_saved_item = saved_users[0]
        second_saved_item = saved_users[1]

        self.assertEqual(self.first_user.username, 'testuser1')
        self.assertEqual(self.second_user.username, 'testuser2')