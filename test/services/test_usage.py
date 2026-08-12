import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.usage import Usage

class UsageServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.usage = Usage(self.client)

    @requests_mock.Mocker()
    def test_list_events(self, m):
        data = {
    "interval": "1d",
    "metrics": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.usage.list_events(
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_gauges(self, m):
        data = {
    "interval": "1d",
    "metrics": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.usage.list_gauges(
            [],
        )

        self.assertEqual(response.to_dict(), data)

