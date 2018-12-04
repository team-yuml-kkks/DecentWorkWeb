from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class UserProfilesTests(APITestCase):
    fixtures = ['users', 'cities', 'professions']

    def setUp(self):
        self.client = APIClient()

    def _get_credentials(self):
        token = Token.objects.get(user=1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_method_status201(self):
        self._get_credentials()
        data = {'description': 'test', 'city': 'Warszawa', 'professions': 'Hydraulik',
                'phone_numbers': '123456789'}
        response = self.client.post('/profiles/userProfiles/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_response_when_success(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'description': 'test', 'city': 'Warszawa', 'professions': ['Hydraulik'],
            'phone_numbers': ['123456789']
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.data['user']['first_name'], 'Test')
        self.assertEqual(response.data['user']['last_name'], 'Test2')
        self.assertEqual(response.data['description'], 'test')
        self.assertEqual(response.data['city'], 'Warszawa')
        self.assertEqual(response.data['professions'][0], 'Hydraulik')

    def test_create_when_no_description(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'professions': ['Hydraulik'],
            'phone_numbers': ['123456789']
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_phone(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'professions': ['Hydraulik'], 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_city(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'professions': ['Hydraulik'], 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_profession(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_last_name(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test'
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_first_name(self):
        self._get_credentials()
        data = {
            'user': {
                'last_name': 'Test2',
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_two_professions(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'professions': ['Hydraulik', 'Elektryk'], 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_data(self):
        self._get_credentials()
        response = self.client.post('/profiles/userProfiles/')
        self.assertEqual(response.status_code, 201)

    def test_create_when_no_token(self):
        data = {
            'user': {
                'last_name': 'Test2',
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_list_200(self):
        response = self.client.get('/profiles/userProfiles/')
        self.assertEqual(response.status_code, 200)
