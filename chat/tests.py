from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from .models import Room

class RoomCreationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_room(self):
        url = reverse('create_room')
        data = {'room_name': 'Test Room'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('room_name', json_response)
        self.assertIn('created', json_response)
        self.assertEqual(json_response['room_name'], 'Test Room')
        self.assertTrue(json_response['created'])

