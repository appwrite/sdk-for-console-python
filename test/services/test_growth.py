import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.growth import Growth


class GrowthServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.growth = Growth(self.client)

    @requests_mock.Mocker()
    def test_create_conversation(self, m):
        data = {
            "type": "support",
            "email": "john@appwrite.io",
            "organizationId": "5e5ea5c16897e",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.growth.create_conversation(
            'support',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.growth.create_installation()
        self.assertEqual(response, data)
