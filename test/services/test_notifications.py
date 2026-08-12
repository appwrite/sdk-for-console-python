import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.notifications import Notifications

class NotificationsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.notifications = Notifications(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
    "total": 5.0,
    "notifications": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.notifications.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "info",
    "channel": "email",
    "resourceType": "users",
    "resourceId": "5e5bb8c16897e",
    "parentResourceType": "projects",
    "parentResourceId": "5e5bb8c16897e",
    "title": "New sign-in detected",
    "body": "A new device signed in to your account."
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.notifications.update(
            '<NOTIFICATION_ID>',
            True,
        )

        self.assertEqual(response.to_dict(), data)

