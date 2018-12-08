from django.test import TestCase, Client

from decentwork.apps.common.models import User


class TestHome(TestCase):
    fixtures = ['users']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(pk=1)

    def test_home_without_login(self):
        """Test home when user is not logged in."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_home_when_user_logged(self):
        """Test status code when user is logged."""
        self.client.force_login(self.user)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template_home(self):
        """Test template of response when user is logged."""
        self.client.force_login(self.user)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_token_in_session(self):
        """Test if token is added to session."""
        self.client.force_login(self.user)
        self.client.get('/')
        session = self.client.session
        self.assertTrue('token' in session)
