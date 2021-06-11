from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from siteusers.models import SiteUsers
from siteusers.views import UserCustomViewSet


class TestUserCustomViewSet(TestCase):

    def test_get_users_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')

        admin = SiteUsers.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')
        force_authenticate(request, admin)

        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail_unauthorized(self):
        user = mixer.blend(SiteUsers)

        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_detail(self):
        user = mixer.blend(SiteUsers)
        admin = SiteUsers.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        client = APIClient()
        client.login(username='admin', password='admin12345')
        response = client.get(f'/api/users/{user.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        client.logout()


class ApiTestUserCustomViewSet(APITestCase):

    def test_get_users_list_unauthorized(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_list(self):
        admin = SiteUsers.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail_unauthorized(self):
        user = mixer.blend(SiteUsers)

        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_detail(self):
        user = mixer.blend(SiteUsers)
        admin = SiteUsers.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_user_admin(self):
        user = mixer.blend(SiteUsers)
        admin = SiteUsers.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')
        response = self.client.patch(f'/api/users/{user.id}/', {'first_name': 'user_test', 'age': 30})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = SiteUsers.objects.get(id=user.id)
        self.assertEqual(user.first_name, 'user_test')
        self.assertEqual(user.age, 30)
