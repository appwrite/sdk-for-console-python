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
            email='email@example.com',
            name='<NAME>',
            subject='<SUBJECT>',
            message='<MESSAGE>',
            organization_id='<ORGANIZATION_ID>',
            project_id='<PROJECT_ID>',
            attributes={},
            attachment=InputFile.from_bytes(bytearray(), "example.file"),
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/growth/conversations',
        )
        sent = dict(
            re.findall(
                r'form-data; name="([^"\[]+)[^\r\n]*\r\n(?:[^\r\n]+\r\n)*\r\n(.*?)\r\n--',
                request.body.decode('latin-1'),
                re.S,
            )
        )
        self.assertEqual(
            sent,
            {
                'type': 'support',
                'email': 'email@example.com',
                'name': '<NAME>',
                'subject': '<SUBJECT>',
                'message': '<MESSAGE>',
                'organizationId': '<ORGANIZATION_ID>',
                'projectId': '<PROJECT_ID>',
                'attachment': '',
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
        response = self.growth.create_installation(
            email='email@example.com',
            name='<NAME>',
            version='<VERSION>',
            domain='<DOMAIN>',
            database='<DATABASE>',
            host_ip='<HOST_IP>',
            user_agent='<USER_AGENT>',
            os='<OS>',
            arch='<ARCH>',
            cpus=1,
            ram=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/growth/installations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'name': '<NAME>',
                'version': '<VERSION>',
                'domain': '<DOMAIN>',
                'database': '<DATABASE>',
                'hostIp': '<HOST_IP>',
                'userAgent': '<USER_AGENT>',
                'os': '<OS>',
                'arch': '<ARCH>',
                'cpus': 1,
                'ram': 1,
            },
        )
        self.assertEqual(response, data)
