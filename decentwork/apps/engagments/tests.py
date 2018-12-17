from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from decentwork.apps.common.models import User


class EngagmentsApiTests(APITestCase):
    fixtures = ['users', 'cities', 'professions', 'engagments', 'userassign']

    def setUp(self):
        self.client = APIClient()

    def _get_credentials(self):
        token = Token.objects.get(user=1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_list_method_status_200(self):
        """Test status 200 when getting /engagments."""
        response = self.client.get('/engagments/engagments/')
        self.assertEqual(response.status_code, 200)

    def test_list_method_response(self):
        """Test response data when getting list of engagments."""
        response = self.client.get('/engagments/engagments/')
        self.assertEqual(response.data['results'][0]['title'], 'Test')
        self.assertEqual(response.data['results'][1]['title'], 'Hello')

    def test_list_method_content_type(self):
        """Test content-type in viewset method."""
        response = self.client.get('/engagments/engagments/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_retrieve_method_status_200(self):
        """Test response status from retrieve viewset method."""
        response = self.client.get('/engagments/engagments/1/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_method_contents_json(self):
        """Test response content-type in retrieve method."""
        response = self.client.get('/engagments/engagments/1/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_retrive_response_json(self):
        """Test response data in retrieve method."""
        response = self.client.get('/engagments/engagments/1/')
        self.assertEqual(response.data['title'], 'Test')

    def test_create_without_token(self):
        response = self.client.post('/engagments/engagments/')
        self.assertEqual(response.status_code, 401)

    def test_create_engagment_when_all_data_pass(self):
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol',
                'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.post('/engagments/engagments/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_engagment_when_no_city(self):
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol',
                'profession': 'Hydraulik'}
        response = self.client.post('/engagments/engagments/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_engagment_when_no_profession(self):
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol', 'city': 'Warszawa'}
        response = self.client.post('/engagments/engagments/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_engagment_when_no_description(self):
        self._get_credentials()
        data = {'title': 'Hello2', 'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.post('/engagments/engagments/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_engagment_when_no_title(self):
        self._get_credentials()
        data = {'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.post('/engagments/engagments/', data)
        self.assertEqual(response.status_code, 400)

    def test_assign_engagment_and_user(self):
        self._get_credentials()
        data = {'engagment': 1}
        response = self.client.post('/engagments/assign/user/', data)
        self.assertEqual(response.status_code, 201)

    def test_delete_assign(self):
        self._get_credentials()
        response = self.client.delete('/engagments/assign/user/2/')
        self.assertEqual(response.status_code, 204)
