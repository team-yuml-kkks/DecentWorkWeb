from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from decentwork.apps.common.models import User


class UserProfilesTests(APITestCase):
    fixtures = ['users', 'cities', 'professions', 'uprofiles']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='lol', password='lol1234#', email='ttt@ttt.ttt')

    def _get_credentials(self, user=None):
        if not user:
            token = Token.objects.get(user=self.user)
        else:
            token = Token.objects.get(user=user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_update_method_status_201(self):
        self._get_credentials()
        data = {'description': 'test', 'city': 'Warszawa', 'professions': 'Hydraulik',
                'phone_numbers': '123456789'}
        response = self.client.put('/profiles/userProfiles/1/', data)
        self.assertEqual(response.status_code, 200)

    def test_update_response_when_success(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'description': 'test', 'city': 'Warszawa', 'professions': ['Hydraulik'],
            'phone_numbers': ['123456789']
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.data['user']['first_name'], 'Test')
        self.assertEqual(response.data['user']['last_name'], 'Test2')
        self.assertEqual(response.data['description'], 'test')
        self.assertEqual(response.data['city'], 'Warszawa')
        self.assertEqual(response.data['professions'][0], 'Hydraulik')

    def test_update_when_no_description(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'professions': ['Hydraulik'],
            'phone_numbers': ['123456789']
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_no_phone(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'professions': ['Hydraulik'], 'description': 'test'
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_no_city(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'professions': ['Hydraulik'], 'description': 'test'
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_no_profession(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_no_last_name(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test'
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_no_first_name(self):
        self._get_credentials()
        data = {
            'user': {
                'last_name': 'Test2',
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_two_professions(self):
        self._get_credentials()
        data = {
            'user': {
                'first_name': 'Test', 'last_name': 'Test2',
            },
            'city': 'Warszawa', 'professions': ['Hydraulik', 'Elektryk'], 'description': 'test'
        }
        response = self.client.put('/profiles/userProfiles/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_when_no_token(self):
        data = {
            'user': {
                'last_name': 'Test2',
            },
            'city': 'Warszawa', 'description': 'test'
        }
        response = self.client.post('/profiles/userProfiles/', data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_list_200(self):
        """Test status of listing users profiles."""
        response = self.client.get('/profiles/userProfiles/')
        self.assertEqual(response.status_code, 200)

    def test_retrive_one_user_profile(self):
        """Test data from retrievieng one user profile."""
        response = self.client.get('/profiles/userProfiles/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['id'], 1)
        self.assertEqual(response.data['city'], None)
        self.assertEqual(response.data['professions'], ['Hydraulik', 'Elektryk'])

    def test_partial_update_city(self):
        """Test update city in profile."""
        data = {'city': 'Łódź'}
        self._get_credentials(1)
        response = self.client.patch('/profiles/userProfiles/1/', data)
        self.assertEqual(response.data['city'], 'Łódź')

    def test_partial_update_professions(self):
        """Test update profile's professions."""
        data = {'professions': 'Murarz'}
        self._get_credentials(1)
        response = self.client.patch('/profiles/userProfiles/1/', data)
        self.assertEqual(response.data['professions'], ['Murarz'])

    def test_four_profiles_status_200(self):
        """Tests if endpoint returns 200."""
        response = self.client.get('/profiles/four/')
        self.assertEqual(response.status_code, 200)

    def test_length_of_response_json_array(self):
        """Test if reponse contains 4 json objects."""
        response = self.client.get('/profiles/four/')
        self.assertEqual(len(response.data), 4)
