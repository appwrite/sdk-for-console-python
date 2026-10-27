import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.create_repository_detection(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
            'runtime',
            provider_root_directory='<PROVIDER_ROOT_DIRECTORY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/detections',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerRepositoryId': '<PROVIDER_REPOSITORY_ID>',
                'type': 'runtime',
                'providerRootDirectory': '<PROVIDER_ROOT_DIRECTORY>',
            },
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_repositories(
            '<INSTALLATION_ID>',
            'runtime',
            search='<SEARCH>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/providerRepositories',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'type': ['runtime'],
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.create_repository(
            '<INSTALLATION_ID>',
            '<NAME>',
            False,
            provider_namespace='<PROVIDER_NAMESPACE>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/providerRepositories',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'private': False,
                'providerNamespace': '<PROVIDER_NAMESPACE>',
            },
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.get_repository(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/providerRepositories/<PROVIDER_REPOSITORY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_repository_branches(self, m):
        data = {
            "total": 5.0,
            "branches": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_repository_branches(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
            search='<SEARCH>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/providerRepositories/<PROVIDER_REPOSITORY_ID>/branches',
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
    def test_get_repository_contents(self, m):
        data = {
            "total": 5.0,
            "contents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.get_repository_contents(
            '<INSTALLATION_ID>',
            '<PROVIDER_REPOSITORY_ID>',
            provider_root_directory='<PROVIDER_ROOT_DIRECTORY>',
            provider_reference='<PROVIDER_REFERENCE>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/providerRepositories/<PROVIDER_REPOSITORY_ID>/contents',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'providerRootDirectory': ['<PROVIDER_ROOT_DIRECTORY>'],
                'providerReference': ['<PROVIDER_REFERENCE>'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_external_deployments(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.update_external_deployments(
            '<INSTALLATION_ID>',
            '<REPOSITORY_ID>',
            '<PROVIDER_PULL_REQUEST_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/github/installations/<INSTALLATION_ID>/repositories/<REPOSITORY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerPullRequestId': '<PROVIDER_PULL_REQUEST_ID>',
            },
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_installations(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/installations',
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
    def test_get_installation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "provider": "github",
            "organization": "appwrite",
            "providerInstallationId": "5322",
            "organizationUrl": "https:\/\/github.com\/appwrite",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.get_installation(
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/installations/<INSTALLATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.delete_installation(
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/installations/<INSTALLATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_namespaces(self, m):
        data = {
            "total": 5.0,
            "namespaces": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vcs.list_namespaces(
            '<INSTALLATION_ID>',
            search='<SEARCH>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/vcs/installations/<INSTALLATION_ID>/namespaces',
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
