import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.vcs import Vcs


class VcsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.vcs = Vcs(self.client)

    @requests_mock.Mocker()
    def test_create_repository_detection(self, m):
        data = {
            "type": "runtime",
            "runtime": "node",
            "entrypoint": "index.js",
            "commands": "npm install && npm run build",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.create_repository_detection(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
            'runtime',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_repositories(self, m):
        data = {
            "total": 5.0,
            "runtimeProviderRepositories": [],
            "type": "runtime",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_repositories(
            '<INSTALLATION_ID>',
            'runtime',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_repository(self, m):
        data = {
            "id": "5e5ea5c16897e",
            "name": "appwrite",
            "organization": "appwrite",
            "provider": "github",
            "private": True,
            "defaultBranch": "main",
            "providerInstallationId": "108104697",
            "authorized": True,
            "pushedAt": "datetime",
            "variables": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.create_repository(
            '<INSTALLATION_ID>',
            '<NAME>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_repository(self, m):
        data = {
            "id": "5e5ea5c16897e",
            "name": "appwrite",
            "organization": "appwrite",
            "provider": "github",
            "private": True,
            "defaultBranch": "main",
            "providerInstallationId": "108104697",
            "authorized": True,
            "pushedAt": "datetime",
            "variables": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.get_repository(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_repository_branches(self, m):
        data = {
            "total": 5.0,
            "branches": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_repository_branches(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_repository_contents(self, m):
        data = {
            "total": 5.0,
            "contents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.get_repository_contents(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_external_deployments(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.update_external_deployments(
            '<INSTALLATION_ID>',
            '<REPOSITORY_ID>',
            '<PROVIDER_PULL_REQUEST_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_installations(self, m):
        data = {
            "total": 5.0,
            "installations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_installations()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_installation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "provider": "github",
            "organization": "appwrite",
            "providerInstallationId": "5322",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.get_installation(
            '<INSTALLATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.delete_installation(
            '<INSTALLATION_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_namespaces(self, m):
        data = {
            "total": 5.0,
            "namespaces": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_namespaces(
            '<INSTALLATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)
