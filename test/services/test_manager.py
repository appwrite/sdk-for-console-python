import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.manager import Manager

class ManagerServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.manager = Manager(self.client)

    @requests_mock.Mocker()
    def test_create_block(self, m):
        data = {
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "resourceType": "project",
    "resourceId": "5e5ea5c16897e",
    "mode": "readOnly",
    "projectName": "My Project",
    "region": "fra",
    "organizationName": "Acme Inc.",
    "organizationId": "5e5ea5c16897e",
    "billingPlan": "pro"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.manager.create_block(
            '<PROJECT_ID>',
            'projects',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_block(self, m):
        data = {
    "deleted": 1.0,
    "blocks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.manager.delete_block(
            '<PROJECT_ID>',
            'projects',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_blocks(self, m):
        data = {
    "total": 5.0,
    "blocks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.manager.list_blocks(
            '<PROJECT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_cache(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.manager.delete_cache(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_user_status(self, m):
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.manager.update_user_status(
            True,
        )

        self.assertEqual(response.to_dict(), data)

