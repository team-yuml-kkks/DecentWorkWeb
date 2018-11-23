from collections import OrderedDict

from django.test import Client, TestCase
from rest_framework.test import APIClient, APITestCase

from decentwork.apps.common.models import User


class UserApiTests(APITestCase):
    fixtures = ['users']

    def setUp(self):
        self.client = Client()
        self.apiclient = APIClient()
        
    def test_list_in_user_viewset(self):
        """Tests response where getting list from viewset."""
        response = self.client.get('/common/users/')
        self.assertEqual(response.data, [OrderedDict([('email', 'test@test.com')])])
    
    def test_creating_new_user(self):
        """Tests creating view in viewset."""
        data = {'email' : 'test2@test2.com', 'password': 'testPassword12#'}
        response = self.client.post('/common/users/', data)
        self.assertEqual(response.status_code, 201)
        user = User.objects.get(email=data['email'])
        self.assertEqual(user.email, data['email'])

    def test_creating_new_user_when_no_email(self):
        """Tests if response has 400 status code when no email POST parameter."""
        data = {'password': 'testPassword12#'}
        response = self.client.post('/common/users/', data)
        self.assertEqual(response.status_code, 400)

    def test_creating_new_user_when_no_password(self):
        """Tests if response has 400 status code when no password POST parameter."""
        data = {'email': 'test2@test2.com'}
        response = self.client.post('/common/users/', data)
        self.assertEqual(response.status_code, 400)
    
    def test_creating_new_user_when_no_both_params(self):
        """Tests if response has 400 status code when no POST parameter."""
        data = {}
        response = self.client.post('/common/users/', data)
        self.assertEqual(response.status_code, 400)

    def test_creating_new_user_when_email_is_not_valid(self):
        """Tests if response status code is 301 when email is not valid."""
        data = {'email' : 'test2est2.com', 'password': 'testPassword12#'}
        response = self.client.post('/common/users', data)
        self.assertEqual(response.status_code, 301)
    
    def test_creating_new_user_when_email_already_exists(self):
        """Tests if response status code is 400 when email already exists in database."""
        data = {'email' : 'test@test.com', 'password': 'testPassword12#'}
        response = self.client.post('/common/users/', data)
        self.assertEqual(response.status_code, 400)
    
    def test_retriving_user(self):
        """Tests response data in retriev view."""
        response = self.client.get('/common/users/1/')
        self.assertEqual(response.data, {'email': 'test@test.com'})

    def test_retriving_user_when_wrong_id(self):
        """Tests if status_code is 404 when no user in database."""
        response = self.client.get('/common/users/2/')
        self.assertEqual(response.status_code, 404)

    def test_update_user_email_only(self):
        """Tests if update user viewset method work for email only."""
        data = {'email': 'test2@test.com'}
        response = self.apiclient.put('/common/users/1/', data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_when_wrong_user(self):
        """Tests if 404 when no user in database."""
        data = {'email': 'test2@test.com'}
        response = self.apiclient.put('/common/users/2/', data)
        self.assertEqual(response.status_code, 404)
