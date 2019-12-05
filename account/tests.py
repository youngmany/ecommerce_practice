from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):

    def test_create_user(self):
        first_user = User()
        first_user.username = 'testuser1'
        first_user.password = '123123'
        first_user.save()

        second_user = User()
        second_user.username = 'testuser2'
        second_user.password = '123123'
        second_user.save()

        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 2)

        first_saved_item = saved_users[0]
        second_saved_item = saved_users[1]

        self.assertEqual(first_user.username, 'testuser1')
        self.assertEqual(second_user.username, 'testuser2')