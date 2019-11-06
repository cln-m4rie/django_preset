from django.test import TestCase

from main.forms import SignupForm


class TestSignupForm(TestCase):
    def test_signup_success(self):
        form_data = {
            'first_name': 'user',
            'last_name': 'test',
            'user_name': 'guest',
            'email': 'test@example.com',
            'password': 'password'}
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_required_first_name(self):
        form_data = {
            'first_name': None,
            'last_name': 'test',
            'user_name': 'guest',
            'email': 'test@example.com',
            'password': 'password'}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_required_last_name(self):
        form_data = {
            'first_name': 'user',
            'last_name': None,
            'user_name': 'guest',
            'email': 'test@example.com',
            'password': 'password'}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_required_email(self):
        form_data = {
            'first_name': 'user',
            'last_name': 'test',
            'user_name': 'guest',
            'email': None,
            'password': 'password'}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_required_password(self):
        form_data = {
            'first_name': 'user',
            'last_name': 'test',
            'user_name': 'guest',
            'email': 'test@example.com',
            'password': None}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_format_email(self):
        form_data = {
            'first_name': 'user',
            'last_name': 'test',
            'user_name': 'guest',
            'email': 'test',
            'password': 'password'}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_less_password(self):
        form_data = {
            'first_name': 'user',
            'last_name': 'test',
            'user_name': 'guest',
            'email': 'test@example.com',
            'password': 'pass'}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
