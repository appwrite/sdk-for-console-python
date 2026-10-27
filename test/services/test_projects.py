import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.projects import Projects


class ProjectsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.projects = Projects(self.client)

    @requests_mock.Mocker()
    def test_list_addons(self, m):
        data = {
            "total": 5.0,
            "addons": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.list_addons(
            '<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/addons',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_premium_geo_db_addon(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "key": "baa",
            "resourceType": "organization",
            "resourceId": "5e5ea5c16897e",
            "status": "active",
            "currentValue": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.create_premium_geo_db_addon(
            '<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/addons/premium-geo-db',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_addon(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "key": "baa",
            "resourceType": "organization",
            "resourceId": "5e5ea5c16897e",
            "status": "active",
            "currentValue": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.get_addon(
            '<PROJECT_ID>',
            '<ADDON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/addons/<ADDON_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_addon(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.delete_addon(
            '<PROJECT_ID>',
            '<ADDON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/addons/<ADDON_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_confirm_addon_payment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "key": "baa",
            "resourceType": "organization",
            "resourceId": "5e5ea5c16897e",
            "status": "active",
            "currentValue": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.confirm_addon_payment(
            '<PROJECT_ID>',
            '<ADDON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/addons/<ADDON_ID>/confirmations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_addon_price(self, m):
        data = {
            "addonKey": "baa",
            "name": "HIPAA BAA",
            "monthlyPrice": 350,
            "proratedAmount": 175.5,
            "remainingDays": 15.0,
            "totalCycleDays": 30.0,
            "currency": "USD",
            "billingCycleEnd": "2024-02-01T00:00:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.get_addon_price(
            '<PROJECT_ID>',
            'baa',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/addons/baa/price',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_console_access(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.update_console_access(
            '<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/console-access',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_schedules(self, m):
        data = {
            "total": 5.0,
            "schedules": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.list_schedules(
            '<PROJECT_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/schedules',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_schedule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "resourceType": "function",
            "resourceId": "5e5ea5c16897e",
            "resourceUpdatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "schedule": "5 4 * * *",
            "data": {},
            "active": True,
            "region": "fra",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.create_schedule(
            '<PROJECT_ID>',
            'function',
            '<RESOURCE_ID>',
            schedule='0 0 * * *',
            active=False,
            data={},
            interval=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/schedules',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resourceType': 'function',
                'resourceId': '<RESOURCE_ID>',
                'schedule': '0 0 * * *',
                'active': False,
                'data': {},
                'interval': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_schedule(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "resourceType": "function",
            "resourceId": "5e5ea5c16897e",
            "resourceUpdatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "schedule": "5 4 * * *",
            "data": {},
            "active": True,
            "region": "fra",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.get_schedule(
            '<PROJECT_ID>',
            '<SCHEDULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/schedules/<SCHEDULE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_stages(self, m):
        data = {
            "stages": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.list_stages(
            '<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/stages',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_stage(self, m):
        data = {
            "id": "tablesDB.create",
            "sdk": "tablesDB.create",
            "status": "completed",
            "at": "2020-10-15T06:38:00.000+00:00",
            "actorType": "user",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.update_stage(
            '<PROJECT_ID>',
            '<STAGE_ID>',
            skip=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/stages/<STAGE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'skip': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_status(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.projects.update_status(
            '<PROJECT_ID>',
            'active',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'status': 'active',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_team(self, m):
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
        response = self.projects.update_team(
            '<PROJECT_ID>',
            '<TEAM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/projects/<PROJECT_ID>/team',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'teamId': '<TEAM_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)
