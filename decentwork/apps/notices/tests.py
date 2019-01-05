from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from decentwork.apps.common.models import User


class NoticesApiTests(APITestCase):
    fixtures = ['users', 'cities', 'professions', 'notices', 'userassign']

    def setUp(self):
        self.client = APIClient()

    def _get_credentials(self):
        token = Token.objects.get(user=1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_list_method_status_200(self):
        """Test status 200 when getting /engagments."""
        response = self.client.get('/notices/notices/')
        self.assertEqual(response.status_code, 200)

    def test_list_method_response(self):
        """Test response data when getting list of engagments."""
        response = self.client.get('/notices/notices/')
        self.assertEqual(response.data['results'][0]['title'], 'Test')
        self.assertEqual(response.data['results'][1]['title'], 'Hello')

    def test_list_method_content_type(self):
        """Test content-type in viewset method."""
        response = self.client.get('/notices/notices/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_retrieve_method_status_200(self):
        """Test response status from retrieve viewset method."""
        response = self.client.get('/notices/notices/1/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_method_contents_json(self):
        """Test response content-type in retrieve method."""
        response = self.client.get('/notices/notices/1/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_retrive_response_json(self):
        """Test response data in retrieve method."""
        response = self.client.get('/notices/notices/1/')
        self.assertEqual(response.data['title'], 'Test')

    def test_create_without_token(self):
        """Test if create returns 401 when no token."""
        response = self.client.post('/notices/notices/')
        self.assertEqual(response.status_code, 401)

    def test_create_engagment_when_all_data_pass(self):
        """Test create returns 201 when all data is good."""
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol',
                'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.post('/notices/notices/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_engagment_when_no_city(self):
        """Test create engagment returns 400 when no city passed."""
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol',
                'profession': 'Hydraulik'}
        response = self.client.post('/notices/notices/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_engagment_when_no_profession(self):
        """Test create engagment returns 201 when no profession is passed."""
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol', 'city': 'Warszawa'}
        response = self.client.post('/notices/notices/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_engagment_when_no_description(self):
        """Test create engagment returns 201 when no description is passed."""
        self._get_credentials()
        data = {'title': 'Hello2', 'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.post('/notices/notices/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_engagment_when_no_title(self):
        """Test create engagment returns 400 when no title passed."""
        self._get_credentials()
        data = {'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.post('/notices/notices/', data)
        self.assertEqual(response.status_code, 400)

    def test_update_engagment(self):
        """Test update engagment returns 200."""
        self._get_credentials()
        data = {'title': 'Hello2', 'description': 'lol',
                'city': 'Warszawa', 'profession': 'Hydraulik'}
        response = self.client.put('/notices/notices/1/', data)
        self.assertEqual(response.status_code, 200)

    def test_assign_engagment_and_user(self):
        """Test assigning engagment with user returns 201."""
        self._get_credentials()
        data = {'notice': 1}
        response = self.client.post('/notices/assign/user/', data)
        self.assertEqual(response.status_code, 201)

    def test_delete_assign(self):
        """Test if deleting assigment between engagment and user returns 204."""
        self._get_credentials()
        response = self.client.delete('/notices/assign/user/2/')
        self.assertEqual(response.status_code, 204)

    def test_assign_list(self):
        """Test showing list of users assigned to single engagment."""
        data = {'notice': 2}
        response = self.client.get('/notices/assign/list/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['notice'], 2)
        self.assertEqual(response.data[0]['user'], 1)
        self.assertEqual(response.data[1]['notice'], 2)
        self.assertEqual(response.data[1]['user'], 3)

    def test_assign_list_when_no_engagment_passed(self):
        """Test if assign list returns 400 when no engagment passed."""
        response = self.client.get('/notices/assign/list/')
        self.assertEqual(response.status_code, 400)

    def test_assign_check_no_engagment(self):
        """Test if assign check returns 400 when no engagment passed."""
        self._get_credentials()
        response = self.client.get('/notices/assign/check/')
        self.assertEqual(response.status_code, 400)

    def test_assign_check_no_credentials(self):
        """Test if assign check returns 401 when no credentials passed."""
        response = self.client.get('/notices/assign/check/')
        self.assertEqual(response.status_code, 401)

    def test_assign_check(self):
        """Test assign_check when success."""
        data = {'notice': 1}
        self._get_credentials()
        response = self.client.get('/notices/assign/check/', data)
        self.assertEqual(response.status_code, 200)

    def test_assign_check_when_not_assigned(self):
        """
        Test if response contains key is_assigned and it contains False
        when user is not assigned to engagment.
        """
        data = {'notice': 1}
        self._get_credentials()
        response = self.client.get('/notices/assign/check/', data)
        self.assertEqual(response.data['is_assigned'], False)

    def test_assign_check_when_assigned(self):
        """
        Test if response contains key is_assigned and it contains True
        when user is assigned to engagment.
        """
        data = {'notice': 2}
        self._get_credentials()
        response = self.client.get('/notices/assign/check/', data)
        self.assertEqual(response.data['is_assigned'], True)
