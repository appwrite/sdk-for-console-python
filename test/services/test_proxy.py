import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.proxy import Proxy


class ProxyServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.proxy = Proxy(self.client)

    @requests_mock.Mocker()
    def test_create_invalidation(self, m):
        data = {
            "domain": "appwrite.company.com",
            "type": "tag",
            "reference": "products",
            "status": "success",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.create_invalidation(
            'example.com',
            'tag',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/invalidations',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'domain',
                'type',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_rules(self, m):
        data = {
            "total": 5.0,
            "rules": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.list_rules()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_api_rule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.create_api_rule(
            'example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/api',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'domain',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_function_rule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.create_function_rule(
            'example.com',
            '<FUNCTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/function',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'domain',
                'functionId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_redirect_rule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.create_redirect_rule(
            'example.com',
            'https://example.com',
            '301',
            '<RESOURCE_ID>',
            'site',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/redirect',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'domain',
                'url',
                'statusCode',
                'resourceId',
                'resourceType',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_site_rule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.create_site_rule(
            'example.com',
            '<SITE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/site',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'domain',
                'siteId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_rule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.create_smtp_rule(
            'example.com',
            '<FUNCTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/smtp',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'domain',
                'functionId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_rule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.get_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/<RULE_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_rule(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.delete_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_rule_status(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "appwrite.company.com",
            "type": "deployment",
            "trigger": "manual",
            "redirectUrl": "https:\/\/appwrite.io\/docs",
            "redirectStatusCode": 301.0,
            "deploymentId": "n3u9feiwmf",
            "deploymentResourceId": "n3u9feiwmf",
            "deploymentVcsProviderBranch": "main",
            "status": "verified",
            "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.proxy.update_rule_status(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/proxy/rules/<RULE_ID>/status',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)
