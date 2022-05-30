from faker import Faker

from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    
    def setUp(self):
        from users.models import User
        
        faker = Faker()
        
        self.login_url = '/login/'
        self.user = User.objects.create_superuser(
            name = 'Admin',
            last_name = 'administo',
            username = faker.name(),
            # username = 'admin',
            password = 'admin123456',
            email = faker.email()
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username': self.user.usernamer,
                'password': 'admin123456'
            },
            format = 'json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.token = response.data['token']
        self.client.credentials(HPPT_AUTHORIZATION = 'Beares ' + self.token)
        
        return super().setUp()
    
    def test_asd(self):
        pass