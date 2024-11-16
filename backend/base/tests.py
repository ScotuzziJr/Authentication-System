from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Note

class UserRegistrationTestCase(APITestCase):
    def test_register_user(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")
        self.assertEqual(User.objects.get().email, "testuser@example.com")


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_login_user(self):
        data = {"username": "testuser", "password": "password123"}
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.cookies)
        self.assertIn("refresh_token", response.cookies)

class TokenRefreshTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        refresh = RefreshToken.for_user(self.user)
        self.client.cookies["refresh_token"] = str(refresh)

    def test_refresh_token(self):
        response = self.client.post('/api/token/refresh/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.cookies)

class LogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        refresh = RefreshToken.for_user(self.user)
        self.client.cookies["access_token"] = str(refresh.access_token)

    def test_logout_user(self):
        response = self.client.post('/api/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["success"], True)

class NotesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.note = Note.objects.create(description="Test Note", owner=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.client.cookies["access_token"] = str(refresh.access_token)

    def test_get_notes_authenticated(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["description"], "Test Note")

    def test_get_notes_unauthenticated(self):
        self.client.cookies.clear()
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
