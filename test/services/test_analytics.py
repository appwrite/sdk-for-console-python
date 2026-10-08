import json
import requests_mock
import unittest

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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_properties()
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
            "public": True,
            "allowedOrigins": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_property(
            '<PROPERTY_ID>',
            '<NAME>',
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
            "public": True,
            "allowedOrigins": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.get_property(
            '<PROPERTY_ID>',
        )
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
            "public": True,
            "allowedOrigins": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.update_property(
            '<PROPERTY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_property(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.delete_property(
            '<PROPERTY_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_event(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_event(
            '<PROPERTY_ID>',
            '<NAME>',
            'https://example.com',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_metrics(
            '<PROPERTY_ID>',
        )
        self.assertEqual(response.to_dict(), data)
