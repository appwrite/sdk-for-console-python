import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.growth.create_conversation(
            'support',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/growth/conversations',
        )
        sent = set(re.findall(r'form-data; name="([^"\[]+)', request.body.decode('latin-1')))
        self.assertEqual(
            sent,
            {
                'type',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.growth.create_installation()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/growth/installations',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)
