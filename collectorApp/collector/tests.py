from django.test import TestCase
from django.contrib.auth import get_user_model

from .forms import UserCreateForm

class UserCreateFormTestCase(TestCase):
    def setUp(self):
        self.form = UserCreateForm()

    def test_form_has_fields(self):
        # Test that the form has the correct fields
        expected_fields = ['username', 'email', 'password1', 'password2']
        self.assertSequenceEqual(expected_fields, list(self.form.fields))
    
    def test_form_validation(self):
        # Test that the form requires all fields to be filled in
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass',
            'password2': 'testpass'
        }
        form = UserCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test that the form requires the passwords to match
        form_data['password2'] = 'wrongpass'
        form = UserCreateForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test that the form requires a unique username
        User = get_user_model()
        User.objects.create_user(username='testuser', password='testpass')
        form_data['username'] = 'testuser'
        form_data['password2'] = 'testpass'
        form = UserCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
