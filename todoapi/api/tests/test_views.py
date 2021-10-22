"""Tests for todoapi Views"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class PingTests(APITestCase):
    """Tests for ping View"""
    def test_ping(self):
        """
        Ensure we receive the ping instance that we get.
        """
        url = reverse('ping-detail', kwargs={'pk': 'test-data'})
        data = {'pong': 'test-data'}

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
