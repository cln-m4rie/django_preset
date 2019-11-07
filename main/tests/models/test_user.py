from django.db.utils import IntegrityError
from django.test import TestCase

from main.models.user import User


class TestUser(TestCase):
    def test_create_user_success(self):
        email = 'test@example.com'
        password = 'testuser'
        user = User.objects.create_user(email, password)
        self.assertTrue(user)

    def test_create_user_fail(self):
        email = 'test@example.com'
        password = 'testuser'
        user = User.objects.create_user(email, password)
        self.assertTrue(user)
        try:
            User.objects.create_user(email, password)
            self.assertTrue(False)
        except IntegrityError:
            self.assertTrue(True)
