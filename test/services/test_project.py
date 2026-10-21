import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.project import Project


class ProjectServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.project = Project(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_auth_method(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_auth_method(
            'email-password',
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/auth-methods/email-password',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_environments(self, m):
        data = {
            "total": 5.0,
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_environments()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_environment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_environment(
            '<ENVIRONMENT_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'environmentId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_environment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_environment(
            '<ENVIRONMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments/<ENVIRONMENT_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_environment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_environment(
            '<ENVIRONMENT_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments/<ENVIRONMENT_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_environment(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_environment(
            '<ENVIRONMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments/<ENVIRONMENT_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_keys(self, m):
        data = {
            "total": 5.0,
            "keys": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_keys()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'keyId',
                'name',
                'scopes',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ephemeral_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_ephemeral_key(
            [],
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/ephemeral',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'scopes',
                'duration',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_key(
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/<KEY_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/<KEY_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
                'scopes',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_key(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_key(
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/<KEY_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_labels(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_labels(
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/labels',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'labels',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mock_phones(self, m):
        data = {
            "total": 5.0,
            "mockNumbers": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_mock_phones()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mock_phone(self, m):
        data = {
            "number": "+1612842323",
            "otp": "123456",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_mock_phone(
            '+12065550100',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'number',
                'otp',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mock_phone(self, m):
        data = {
            "number": "+1612842323",
            "otp": "123456",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_mock_phone(
            '+12065550100',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones/+12065550100',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mock_phone(self, m):
        data = {
            "number": "+1612842323",
            "otp": "123456",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_mock_phone(
            '+12065550100',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones/+12065550100',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'otp',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_mock_phone(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_mock_phone(
            '+12065550100',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones/+12065550100',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_o_auth2_providers(self, m):
        data = {
            "total": 5.0,
            "providers": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_o_auth2_providers()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_server(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_server(
            True,
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2-server',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
                'authorizationUrl',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_amazon(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "amzn1.application-oa2-client.87400c00000000000000000000063d5b2",
            "clientSecret": "79ffe4000000000000000000000000000000000000000000000000000002de55",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_amazon()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/amazon',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_apple(self, m):
        data = {
            "$id": "apple",
            "enabled": True,
            "serviceId": "ip.appwrite.app.web",
            "keyId": "P4000000N8",
            "teamId": "D4000000R6",
            "p8File": "-----BEGIN PRIVATE KEY-----MIGTAg...jy2Xbna-----END PRIVATE KEY-----",
            "nativeEnabled": True,
            "nativeClientIds": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_apple()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/apple',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_appwrite(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "6a42000000000000b5a0",
            "clientSecret": "b86afd000000000000000000000000000000000000000000000000000ced5f93",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_appwrite()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/appwrite',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_auth0(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "OaOkIA000000000000000000005KLSYq",
            "clientSecret": "zXz0000-00000000000000000000000000000-00000000000000000000PJafnF",
            "prompt": [],
            "endpoint": "example.us.auth0.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_auth0()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/auth0',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_authentik(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "dTKOPa0000000000000000000000000000e7G8hv",
            "clientSecret": "ntQadq000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Hp5WK",
            "endpoint": "example.authentik.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_authentik()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/authentik',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_autodesk(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "5zw90v00000000000000000000kVYXN7",
            "clientSecret": "7I000000000000MW",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_autodesk()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/autodesk',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_bitbucket(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "key": "Knt70000000000ByRc",
            "secret": "NMfLZJ00000000000000000000TLQdDx",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_bitbucket()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/bitbucket',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_bitly(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "d95151000000000000000000000000000067af9b",
            "clientSecret": "a13e250000000000000000000000000000d73095",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_bitly()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/bitly',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_box(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "deglcs00000000000000000000x2og6y",
            "clientSecret": "OKM1f100000000000000000000eshEif",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_box()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/box',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_cloudflare(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "4b866000000000000000000000c9e4e2",
            "clientSecret": "cfoc_5Q6YRl0000000000000000000000000000000000003d214f",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_cloudflare()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/cloudflare',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_dailymotion(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "apiKey": "07a9000000000000067f",
            "apiSecret": "a399a90000000000000000000000000000d90639",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_dailymotion()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/dailymotion',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_discord(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "950722000000343754",
            "clientSecret": "YmPXnM000000000000000000002zFg5D",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_discord()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/discord',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_disqus(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "publicKey": "cgegH70000000000000000000000000000000000000000000000000000Hr1nYX",
            "secretKey": "W7Bykj00000000000000000000000000000000000000000000000000003o43w9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_disqus()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/disqus',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_dropbox(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "appKey": "jl000000000009t",
            "appSecret": "g200000000000vw",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_dropbox()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/dropbox',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_etsy(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "keyString": "nsgzxh0000000000008j85a2",
            "sharedSecret": "tp000000ru",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_etsy()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/etsy',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_facebook(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "appId": "260600000007694",
            "appSecret": "2d0b2800000000000000000000d38af4",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_facebook()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/facebook',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_figma(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "byay5H0000000000VtiI40",
            "clientSecret": "yEpOYn0000000000000000004iIsU5",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_figma()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/figma',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_fusion_auth(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "b2222c00-0000-0000-0000-000000862097",
            "clientSecret": "Jx4s0C0000000000000000000000000000000wGqLsc",
            "endpoint": "example.fusionauth.io",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_fusion_auth()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/fusionauth',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_git_hub(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "e4d87900000000540733",
            "clientSecret": "5e07c00000000000000000000000000000198bcc",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_git_hub()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/github',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_gitlab(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "applicationId": "d41ffe0000000000000000000000000000000000000000000000000000d5e252",
            "secret": "gloas-838cfa0000000000000000000000000000000000000000000000000000ecbb38",
            "endpoint": "https:\/\/gitlab.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_gitlab()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/gitlab',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_google(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "120000000095-92ifjb00000000000000000000g7ijfb.apps.googleusercontent.com",
            "clientSecret": "GOCSPX-2k8gsR0000000000000000VNahJj",
            "prompt": [],
            "nativeEnabled": True,
            "nativeClientIds": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_google()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/google',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_hugging_face(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "2ab9cff9-d711-40ad-a91e-b08a49c42d24",
            "clientSecret": "oauth_app_secret_wcLhRtl000000000000000000000xbNdLt",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_hugging_face()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/huggingface',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_kakao(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "839ff5000000000000000000013206de",
            "clientSecret": "jLNVOK00000000000000000000yJebea",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_kakao()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/kakao',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_keycloak(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "appwrite-o0000000st-app",
            "clientSecret": "jdjrJd00000000000000000000HUsaZO",
            "endpoint": "keycloak.example.com",
            "realmName": "appwrite-realm",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_keycloak()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/keycloak',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_kick(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "01KQ7C00000000000001MFHS32",
            "clientSecret": "34ac5600000000000000000000000000000000000000000000000000e830c8b",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_kick()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/kick',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_linkedin(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "770000000000dv",
            "primaryClientSecret": "WPL_AP1.2Bf0000000000000.\/HtlYw==",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_linkedin()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/linkedin',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_microsoft(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "applicationId": "00001111-aaaa-2222-bbbb-3333cccc4444",
            "applicationSecret": "A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
            "prompt": [],
            "tenant": "common",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_microsoft()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/microsoft',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_notion(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "oauthClientId": "341d8700-0000-0000-0000-000000446ee3",
            "oauthClientSecret": "secret_dLUr4b000000000000000000000000000000lFHAa9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_notion()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/notion',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_oidc(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "qibI2x0000000000000000000000000006L2YFoG",
            "clientSecret": "Ah68ed000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003qpcHV",
            "prompt": [],
            "wellKnownURL": "https:\/\/myoauth.com\/.well-known\/openid-configuration",
            "authorizationURL": "https:\/\/myoauth.com\/oauth2\/authorize",
            "tokenURL": "https:\/\/myoauth.com\/oauth2\/token",
            "userInfoURL": "https:\/\/myoauth.com\/oauth2\/userinfo",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_oidc()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/oidc',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_okta(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "0oa00000000000000698",
            "clientSecret": "Kiq0000000000000000000000000000000000000-00000000000H2L5-3SJ-vRV",
            "prompt": [],
            "domain": "trial-6400025.okta.com",
            "authorizationServerId": "aus000000000000000h7z",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_okta()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/okta',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_paypal(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB",
            "secretKey": "EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_paypal()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/paypal',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_paypal_sandbox(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB",
            "secretKey": "EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_paypal_sandbox()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/paypalSandbox',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_podio(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "appwrite-oauth-test-app",
            "clientSecret": "Rn247T0000000000000000000000000000000000000000000000000000W2zWTN",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_podio()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/podio',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_resend(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
            "clientSecret": "9c1e4b00000000000000000000000000000000000000000000000000a72d5f4",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_resend()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/resend',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_salesforce(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "customerKey": "3MVG9I0000000000000000000000000000000000000000000000000000000000000000000000000C5Aejq",
            "customerSecret": "3w000000000000e2",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_salesforce()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/salesforce',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_slack(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "23000000089.15000000000023",
            "clientSecret": "81656000000000000000000000f3d2fd",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_slack()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/slack',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_spotify(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "6ec271000000000000000000009beace",
            "clientSecret": "db068a000000000000000000008b5b9f",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_spotify()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/spotify',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_stripe(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "ca_UKibXX0000000000000000000006byvR",
            "apiSecretKey": "sk_51SfOd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000QGWYfp",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_stripe()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/stripe',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tik_tok(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "awz000000000tyw0",
            "clientSecret": "6wXewM00000000000000000000yXnite",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_tik_tok()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/tiktok',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tradeshift(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "oauth2ClientId": "appwrite-test-org.appwrite-test-app",
            "oauth2ClientSecret": "7cb52700-0000-0000-0000-000000ca5b83",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_tradeshift()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/tradeshift',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tradeshift_sandbox(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "oauth2ClientId": "appwrite-test-org.appwrite-test-app",
            "oauth2ClientSecret": "7cb52700-0000-0000-0000-000000ca5b83",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_tradeshift_sandbox()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/tradeshiftBox',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_twitch(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "vvi0in000000000000000000ikmt9p",
            "clientSecret": "pmapue000000000000000000zylw3v",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_twitch()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/twitch',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_webflow(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "8bb20000000000000000000000000000000000000000000000000000000040dd",
            "clientSecret": "59bf00000000000000000000000000000000000000000000000000000000fe59",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_webflow()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/webflow',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_word_press(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "130005",
            "clientSecret": "PlBfJS0000000000000000000000000000000000000000000000000000EdUZJk",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_word_press()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/wordpress',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_x(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "customerKey": "slzZV0000000000000NFLaWT",
            "secretKey": "tkEPkp00000000000000000000000000000000000000FTxbI9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_x()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/x',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_yahoo(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "dj0yJm000000000000000000000000000000000000000000000000000000000000000000000000000000000000Z4PWRm",
            "clientSecret": "cf978f0000000000000000000000000000c5e2e9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_yahoo()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/yahoo',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_yandex(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "6a8a6a0000000000000000000091483c",
            "clientSecret": "bbf98500000000000000000000c75a63",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_yandex()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/yandex',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_zoho(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "1000.83C178000000000000000000RPNX0B",
            "clientSecret": "fb5cac000000000000000000000000000000a68f6e",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_zoho()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/zoho',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_zoom(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "QMAC00000000000000w0AQ",
            "clientSecret": "GAWsG4000000000000000000007U01ON",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_zoom()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/zoom',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_o_auth2_provider(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "e4d87900000000540733",
            "clientSecret": "5e07c00000000000000000000000000000198bcc",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_o_auth2_provider(
            'amazon',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/amazon',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_platforms(self, m):
        data = {
            "total": 5.0,
            "platforms": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_platforms()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_android_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "applicationId": "com.company.appname",
            "fingerprints": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_android_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<APPLICATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/android',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'platformId',
                'name',
                'applicationId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_android_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "applicationId": "com.company.appname",
            "fingerprints": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_android_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<APPLICATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/android/<PLATFORM_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
                'applicationId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apple_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "bundleIdentifier": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_apple_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<BUNDLE_IDENTIFIER>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/apple',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'platformId',
                'name',
                'bundleIdentifier',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apple_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "bundleIdentifier": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_apple_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<BUNDLE_IDENTIFIER>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/apple/<PLATFORM_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
                'bundleIdentifier',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_linux_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_linux_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/linux',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'platformId',
                'name',
                'packageName',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_linux_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_linux_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/linux/<PLATFORM_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
                'packageName',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_web_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "hostname": "app.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_web_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            'app.example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/web',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'platformId',
                'name',
                'hostname',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_web_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "hostname": "app.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_web_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            'app.example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/web/<PLATFORM_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
                'hostname',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_windows_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageIdentifierName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_windows_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_IDENTIFIER_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/windows',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'platformId',
                'name',
                'packageIdentifierName',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_windows_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageIdentifierName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_windows_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_IDENTIFIER_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/windows/<PLATFORM_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'name',
                'packageIdentifierName',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "hostname": "app.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_platform(
            '<PLATFORM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/<PLATFORM_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_platform(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_platform(
            '<PLATFORM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/<PLATFORM_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_policies(self, m):
        data = {
            "total": 10.0,
            "policies": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_policies()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_aliased_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_aliased_email_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-aliased-email',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_corporate_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_corporate_email_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-corporate-email',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_disposable_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_disposable_email_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-disposable-email',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_free_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_free_email_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-free-email',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_membership_privacy_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_membership_privacy_policy()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/membership-privacy',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_factors_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_mfa_factors_policy()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/mfa-factors',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_passkey_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_passkey_policy(
            '<RP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/passkey',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'rpId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_dictionary_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_dictionary_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-dictionary',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_history_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_history_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-history',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'total',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_personal_data_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_personal_data_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-personal-data',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_pwned_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_pwned_policy()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-pwned',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_rotation_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_rotation_policy()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-rotation',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_strength_policy(self, m):
        data = {
            "$id": "password-dictionary",
            "min": 12.0,
            "uppercase": True,
            "lowercase": True,
            "number": True,
            "symbols": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_strength_policy()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-strength',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_alert_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_alert_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-alert',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_duration_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_duration_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-duration',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'duration',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_invalidation_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_invalidation_policy(
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-invalidation',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_limit_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_limit_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-limit',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'total',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_user_limit_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_user_limit_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/user-limit',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'total',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_policy(self, m):
        data = {
            "$id": "password-dictionary",
            "enabled": True,
            "denyList": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_policy(
            'password-dictionary',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-dictionary',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_protocol(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_protocol(
            'rest',
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/protocols/rest',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_service(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_service(
            'account',
            True,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/services/account',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'enabled',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_smtp()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/smtp',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_test(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_smtp_test(
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/smtp/tests',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'emails',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_email_templates(self, m):
        data = {
            "total": 5.0,
            "templates": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_email_templates()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/templates/email',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_template(self, m):
        data = {
            "templateId": "verification",
            "locale": "en_us",
            "message": "Click on the link to verify your account.",
            "senderName": "My User",
            "senderEmail": "mail@appwrite.io",
            "replyToEmail": "emails@appwrite.io",
            "replyToName": "Support Team",
            "subject": "Please verify your email address",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_email_template(
            'verification',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/templates/email',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'templateId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_email_template(self, m):
        data = {
            "templateId": "verification",
            "locale": "en_us",
            "message": "Click on the link to verify your account.",
            "senderName": "My User",
            "senderEmail": "mail@appwrite.io",
            "replyToEmail": "emails@appwrite.io",
            "replyToName": "Support Team",
            "subject": "Please verify your email address",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_email_template(
            'verification',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/templates/email/verification',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_variables(self, m):
        data = {
            "total": 5.0,
            "variables": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_variables()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_variable(
            '<VARIABLE_ID>',
            '<KEY>',
            '<VALUE>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'variableId',
                'key',
                'value',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_variable(
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables/<VARIABLE_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_variable(
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables/<VARIABLE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_variable(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_variable(
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables/<VARIABLE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)
