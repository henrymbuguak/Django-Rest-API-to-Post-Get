from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import Bucketlist

class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = "Write code to test your app"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_buckeklist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {"name": "Go to Google"}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
            )

    def test_api_create_a_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
