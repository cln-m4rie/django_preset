from django.test import Client, TestCase

from main.models.user import User


class TestLogin(TestCase):
    def test_unauthorized(self):
        client = Client()
        res = client.get('/')
        self.assertFalse(res.context['user'].is_authenticated)

    def test_authorized(self):
        client = Client()
        client.force_login(User.objects.create_user(
            'test@example.com', 'testuser'))
        response = client.get('/')
        self.assertTrue(response.context['user'].is_authenticated)
