import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            "interval": "1h",
            "metrics": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.usage.list_events(
            [],
            queries=[],
            interval='1m',
            dimensions=[],
            start_at='2020-10-15T06:38:00.000+00:00',
            end_at='2020-10-15T06:38:00.000+00:00',
            order_by='time',
            order_dir='asc',
            limit=1,
            offset=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/usage/events',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'interval': ['1m'],
                'startAt': ['2020-10-15T06:38:00.000+00:00'],
                'endAt': ['2020-10-15T06:38:00.000+00:00'],
                'orderBy': ['time'],
                'orderDir': ['asc'],
                'limit': ['1'],
                'offset': ['1'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_gauges(self, m):
        data = {
            "interval": "1h",
            "metrics": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.usage.list_gauges(
            [],
            queries=[],
            interval='1m',
            dimensions=[],
            start_at='2020-10-15T06:38:00.000+00:00',
            end_at='2020-10-15T06:38:00.000+00:00',
            order_by='time',
            order_dir='asc',
            limit=1,
            offset=1,
            aggregate='last',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/usage/gauges',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'interval': ['1m'],
                'startAt': ['2020-10-15T06:38:00.000+00:00'],
                'endAt': ['2020-10-15T06:38:00.000+00:00'],
                'orderBy': ['time'],
                'orderDir': ['asc'],
                'limit': ['1'],
                'offset': ['1'],
                'aggregate': ['last'],
            },
        )
        self.assertEqual(response.to_dict(), data)
