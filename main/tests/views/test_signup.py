from django.test import TestCase
from django.urls import reverse

from main.forms.signup import SignupForm


class TestSignup(TestCase):
    def setUp(self):
        url = reverse('main:signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_has_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignupForm)

    def test_signup_success(self):
        data = {
            'first_name': 'guest',
            'last_name': 'user',
            'user_name': 'guest user',
            'email': 'test@example.com',
            'password': 'testuser'
        }
        url = reverse('main:signup')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_signup_failed(self):
        data = {
            'first_name': 'guest',
            'last_name': 'user',
            'user_name': 'guest user',
            'email': 'test@example.com',
            'password': 'testuser'
        }
        url = reverse('main:signup')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.client.logout()
        data = {
            'first_name': 'guest',
            'last_name': 'user',
            'user_name': 'guest user',
            'email': 'test@example.com',
            'password': 'testuser'
        }
        url = reverse('main:signup')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
