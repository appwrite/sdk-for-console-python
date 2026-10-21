import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.locale import Locale


class LocaleServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.locale = Locale(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "ip": "127.0.0.1",
            "countryCode": "US",
            "country": "United States",
            "continentCode": "NA",
            "continent": "North America",
            "eu": True,
            "currency": "USD",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.get()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_codes(self, m):
        data = {
            "total": 5.0,
            "localeCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/codes',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_continents(self, m):
        data = {
            "total": 5.0,
            "continents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_continents()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/continents',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_countries(self, m):
        data = {
            "total": 5.0,
            "countries": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_countries()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/countries',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_countries_eu(self, m):
        data = {
            "total": 5.0,
            "countries": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_countries_eu()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/countries/eu',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_countries_phones(self, m):
        data = {
            "total": 5.0,
            "phones": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_countries_phones()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/countries/phones',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_currencies(self, m):
        data = {
            "total": 5.0,
            "currencies": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_currencies()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/currencies',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_languages(self, m):
        data = {
            "total": 5.0,
            "languages": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.locale.list_languages()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/locale/languages',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)
