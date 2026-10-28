import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.analytics import Analytics


class AnalyticsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.analytics = Analytics(self.client)

    @requests_mock.Mocker()
    def test_list_properties(self, m):
        data = {
            "total": 5.0,
            "properties": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_properties(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_property(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Website",
            "domain": "example.com",
            "enabled": True,
            "allowedOrigins": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_property(
            '<PROPERTY_ID>',
            '<NAME>',
            domain='<DOMAIN>',
            enabled=False,
            allowed_origins=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'propertyId': '<PROPERTY_ID>',
                'name': '<NAME>',
                'domain': '<DOMAIN>',
                'enabled': False,
                'allowedOrigins': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_property(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Website",
            "domain": "example.com",
            "enabled": True,
            "allowedOrigins": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.get_property(
            '<PROPERTY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_property(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Website",
            "domain": "example.com",
            "enabled": True,
            "allowedOrigins": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.update_property(
            '<PROPERTY_ID>',
            name='<NAME>',
            domain='<DOMAIN>',
            enabled=False,
            allowed_origins=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'domain': '<DOMAIN>',
                'enabled': False,
                'allowedOrigins': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_property(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.delete_property(
            '<PROPERTY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_event(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_event(
            '<PROPERTY_ID>',
            '<NAME>',
            'https://example.com',
            domain='<DOMAIN>',
            referrer='<REFERRER>',
            screen_width=1,
            session_hash='<SESSION_HASH>',
            scroll_depth=1,
            engagement_time=1,
            props=[],
            user_id='<USER_ID>',
            ip='<IP>',
            user_agent='<USER_AGENT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/events',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'url': 'https://example.com',
                'domain': '<DOMAIN>',
                'referrer': '<REFERRER>',
                'screenWidth': 1,
                'sessionHash': '<SESSION_HASH>',
                'scrollDepth': 1,
                'engagementTime': 1,
                'props': [],
                'userId': '<USER_ID>',
                'ip': '<IP>',
                'userAgent': '<USER_AGENT>',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_metrics(self, m):
        data = {
            "total": 30.0,
            "metrics": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_metrics(
            '<PROPERTY_ID>',
            queries=[],
            interval='1h',
            dimensions=[],
            date_range='<DATE_RANGE>',
            start_at='2020-10-15T06:38:00.000+00:00',
            end_at='2020-10-15T06:38:00.000+00:00',
            limit=1,
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/metrics',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'interval': ['1h'],
                'dateRange': ['<DATE_RANGE>'],
                'startAt': ['2020-10-15T06:38:00.000+00:00'],
                'endAt': ['2020-10-15T06:38:00.000+00:00'],
                'limit': ['1'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)
