import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.messaging import Messaging


class MessagingServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.messaging = Messaging(self.client)

    @requests_mock.Mocker()
    def test_list_messages(self, m):
        data = {
            "total": 5.0,
            "messages": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_messages()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_email(
            '<MESSAGE_ID>',
            '<SUBJECT>',
            '<CONTENT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/email',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'messageId',
                'subject',
                'content',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_email(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/email/<MESSAGE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_push(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_push(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/push',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'messageId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_push(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_push(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/push/<MESSAGE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sms(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'messageId',
                'content',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sms(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'messageId',
                'content',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_sms(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_sms(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms/<MESSAGE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_sms(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_sms(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms/<MESSAGE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_message(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_message(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/<MESSAGE_ID>',
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
        response = self.messaging.delete(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/<MESSAGE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_targets(self, m):
        data = {
            "total": 5.0,
            "targets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_targets(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/<MESSAGE_ID>/targets',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_providers(self, m):
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
        response = self.messaging.list_providers()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apns_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apns_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apns_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apns_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_appwrite_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_appwrite_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/appwrite',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_appwrite_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_appwrite_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/appwrite/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_fcm_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_fcm_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_fcm_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_fcm_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mailgun_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_mailgun_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/mailgun',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mailgun_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_mailgun_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/mailgun/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_msg91_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_msg91_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/msg91',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_msg91_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_msg91_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/msg91/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_resend_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_resend_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/resend',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_resend_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_resend_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/resend/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sendgrid_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_sendgrid_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/sendgrid',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_sendgrid_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_sendgrid_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/sendgrid/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ses_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_ses_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/ses',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_ses_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_ses_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/ses/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
                'host',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
                'host',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_telesign_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_telesign_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/telesign',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_telesign_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_telesign_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/telesign/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_textmagic_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_textmagic_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/textmagic',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_textmagic_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_textmagic_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/textmagic/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_twilio_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_twilio_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/twilio',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_twilio_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_twilio_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/twilio/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_vonage_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_vonage_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/vonage',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'providerId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_vonage_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_vonage_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/vonage/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_provider(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/<PROVIDER_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_provider(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.delete_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/<PROVIDER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_topics(self, m):
        data = {
            "total": 5.0,
            "topics": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_topics()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_topic(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "events",
            "description": "Order status updates sent to customers.",
            "emailTotal": 100.0,
            "smsTotal": 100.0,
            "pushTotal": 100.0,
            "subscribe": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_topic(
            '<TOPIC_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'topicId',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_topic(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "events",
            "description": "Order status updates sent to customers.",
            "emailTotal": 100.0,
            "smsTotal": 100.0,
            "pushTotal": 100.0,
            "subscribe": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_topic(
            '<TOPIC_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_topic(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "events",
            "description": "Order status updates sent to customers.",
            "emailTotal": 100.0,
            "smsTotal": 100.0,
            "pushTotal": 100.0,
            "subscribe": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_topic(
            '<TOPIC_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_topic(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.delete_topic(
            '<TOPIC_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_subscribers(self, m):
        data = {
            "total": 5.0,
            "subscribers": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_subscribers(
            '<TOPIC_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_subscriber(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "targetId": "259125845563242502",
            "target": {
                "$id": "259125845563242502",
                "$createdAt": "2020-10-15T06:38:00.000+00:00",
                "$updatedAt": "2020-10-15T06:38:00.000+00:00",
                "name": "Apple iPhone 12",
                "userId": "259125845563242502",
                "providerType": "email",
                "identifier": "token",
                "expired": True,
            },
            "userId": "5e5ea5c16897e",
            "userName": "Aegon Targaryen",
            "topicId": "259125845563242502",
            "providerType": "email",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
            '<TARGET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'subscriberId',
                'targetId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_subscriber(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "targetId": "259125845563242502",
            "target": {
                "$id": "259125845563242502",
                "$createdAt": "2020-10-15T06:38:00.000+00:00",
                "$updatedAt": "2020-10-15T06:38:00.000+00:00",
                "name": "Apple iPhone 12",
                "userId": "259125845563242502",
                "providerType": "email",
                "identifier": "token",
                "expired": True,
            },
            "userId": "5e5ea5c16897e",
            "userName": "Aegon Targaryen",
            "topicId": "259125845563242502",
            "providerType": "email",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers/<SUBSCRIBER_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_subscriber(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.delete_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers/<SUBSCRIBER_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)
