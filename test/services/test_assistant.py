import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.assistant import Assistant

class AssistantServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.assistant = Assistant(self.client)

    @requests_mock.Mocker()
    def test_chat(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.assistant.chat(
            '<PROMPT>',
        )

        self.assertEqual(response, data)

