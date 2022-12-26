from django.test import TestCase
from django.urls import reverse

from groups.models import User
# Create your tests here.

class LoginTestCase(TestCase):
    def setUp(self):
        # Create a user
        User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):
        # Send a POST request to the login URL with the user's credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the user was authenticated and is now logged in
        self.assertTrue(response.context['user'].is_authenticated)