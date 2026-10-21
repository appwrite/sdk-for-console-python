import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.avatars import Avatars


class AvatarsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.avatars = Avatars(self.client)

    @requests_mock.Mocker()
    def test_get_browser(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_browser(
            'aa',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/browsers/aa',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_credit_card(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_credit_card(
            'amex',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/credit-cards/amex',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_favicon(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_favicon(
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/favicon',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'url',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_flag(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_flag(
            'af',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/flags/af',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_image(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_image(
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/image',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'url',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_initials(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_initials()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/initials',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_photo(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_photo()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/photo',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_photo(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "John Doe",
            "registration": "2020-10-15T06:38:00.000+00:00",
            "status": True,
            "labels": [],
            "passwordUpdate": "2020-10-15T06:38:00.000+00:00",
            "email": "john@appwrite.io",
            "phone": "+4930901820",
            "emailVerification": True,
            "phoneVerification": True,
            "mfa": True,
            "prefs": {},
            "targets": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.avatars.update_photo(
            InputFile.from_bytes(bytearray(), "example.file"),
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/photo',
        )
        sent = set(re.findall(r'form-data; name="([^"\[]+)', request.body.decode('latin-1')))
        self.assertEqual(
            sent,
            {
                'file',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_photo(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.avatars.delete_photo()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/photo',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_qr(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_qr(
            '<TEXT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/qr',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'text',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_screenshot(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_screenshot(
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/screenshots',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'url',
            },
        )
        self.assertEqual(response, data)
