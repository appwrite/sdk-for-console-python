import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.migrations import Migrations


class MigrationsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.migrations = Migrations(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "migrations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.list()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_appwrite_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_appwrite_migration(
            [],
            'https://example.com',
            '<PROJECT_ID>',
            '<API_KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/appwrite',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'resources',
                'endpoint',
                'projectId',
                'apiKey',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_appwrite_report(self, m):
        data = {
            "user": 20.0,
            "team": 20.0,
            "database": 20.0,
            "row": 20.0,
            "file": 20.0,
            "bucket": 20.0,
            "function": 20.0,
            "platform": 5.0,
            "api-key": 5.0,
            "project-variable": 5.0,
            "webhook": 5.0,
            "auth-methods": 1.0,
            "project-protocols": 1.0,
            "project-labels": 1.0,
            "project-services": 1.0,
            "policies": 1.0,
            "smtp": 1.0,
            "rule": 5.0,
            "project-email-template": 7.0,
            "project-environment": 2.0,
            "site": 5.0,
            "provider": 5.0,
            "topic": 10.0,
            "subscriber": 100.0,
            "message": 50.0,
            "size": 30000.0,
            "version": "1.4.0",
            "oauth2-provider": 5.0,
            "backup-policy": 5.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get_appwrite_report(
            [],
            'https://example.com',
            '<PROJECT_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/appwrite/report',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'endpoint',
                'projectID',
                'key',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_csv_export(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_csv_export(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<FILENAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/csv/exports',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'databaseId',
                'collectionId',
                'filename',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_csv_import(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_csv_import(
            '<BUCKET_ID>',
            '<FILE_ID>',
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/csv/imports',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'bucketId',
                'fileId',
                'databaseId',
                'collectionId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_firebase_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_firebase_migration(
            [],
            '<SERVICE_ACCOUNT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/firebase',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'resources',
                'serviceAccount',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_firebase_report(self, m):
        data = {
            "user": 20.0,
            "team": 20.0,
            "database": 20.0,
            "row": 20.0,
            "file": 20.0,
            "bucket": 20.0,
            "function": 20.0,
            "platform": 5.0,
            "api-key": 5.0,
            "project-variable": 5.0,
            "webhook": 5.0,
            "auth-methods": 1.0,
            "project-protocols": 1.0,
            "project-labels": 1.0,
            "project-services": 1.0,
            "policies": 1.0,
            "smtp": 1.0,
            "rule": 5.0,
            "project-email-template": 7.0,
            "project-environment": 2.0,
            "site": 5.0,
            "provider": 5.0,
            "topic": 10.0,
            "subscriber": 100.0,
            "message": 50.0,
            "size": 30000.0,
            "version": "1.4.0",
            "oauth2-provider": 5.0,
            "backup-policy": 5.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get_firebase_report(
            [],
            '<SERVICE_ACCOUNT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/firebase/report',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'serviceAccount',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_json_export(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_json_export(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<FILENAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/json/exports',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'databaseId',
                'collectionId',
                'filename',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_json_import(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_json_import(
            '<BUCKET_ID>',
            '<FILE_ID>',
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/json/imports',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'bucketId',
                'fileId',
                'databaseId',
                'collectionId',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_n_host_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_n_host_migration(
            [],
            '<SUBDOMAIN>',
            '<REGION>',
            '<ADMIN_SECRET>',
            '<DATABASE>',
            '<USERNAME>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/nhost',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'resources',
                'subdomain',
                'region',
                'adminSecret',
                'database',
                'username',
                'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_n_host_report(self, m):
        data = {
            "user": 20.0,
            "team": 20.0,
            "database": 20.0,
            "row": 20.0,
            "file": 20.0,
            "bucket": 20.0,
            "function": 20.0,
            "platform": 5.0,
            "api-key": 5.0,
            "project-variable": 5.0,
            "webhook": 5.0,
            "auth-methods": 1.0,
            "project-protocols": 1.0,
            "project-labels": 1.0,
            "project-services": 1.0,
            "policies": 1.0,
            "smtp": 1.0,
            "rule": 5.0,
            "project-email-template": 7.0,
            "project-environment": 2.0,
            "site": 5.0,
            "provider": 5.0,
            "topic": 10.0,
            "subscriber": 100.0,
            "message": 50.0,
            "size": 30000.0,
            "version": "1.4.0",
            "oauth2-provider": 5.0,
            "backup-policy": 5.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get_n_host_report(
            [],
            '<SUBDOMAIN>',
            '<REGION>',
            '<ADMIN_SECRET>',
            '<DATABASE>',
            '<USERNAME>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/nhost/report',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'subdomain',
                'region',
                'adminSecret',
                'database',
                'username',
                'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_supabase_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_supabase_migration(
            [],
            'https://example.com',
            '<API_KEY>',
            '<DATABASE_HOST>',
            '<USERNAME>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/supabase',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'resources',
                'endpoint',
                'apiKey',
                'databaseHost',
                'username',
                'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_supabase_report(self, m):
        data = {
            "user": 20.0,
            "team": 20.0,
            "database": 20.0,
            "row": 20.0,
            "file": 20.0,
            "bucket": 20.0,
            "function": 20.0,
            "platform": 5.0,
            "api-key": 5.0,
            "project-variable": 5.0,
            "webhook": 5.0,
            "auth-methods": 1.0,
            "project-protocols": 1.0,
            "project-labels": 1.0,
            "project-services": 1.0,
            "policies": 1.0,
            "smtp": 1.0,
            "rule": 5.0,
            "project-email-template": 7.0,
            "project-environment": 2.0,
            "site": 5.0,
            "provider": 5.0,
            "topic": 10.0,
            "subscriber": 100.0,
            "message": 50.0,
            "size": 30000.0,
            "version": "1.4.0",
            "oauth2-provider": 5.0,
            "backup-policy": 5.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get_supabase_report(
            [],
            'https://example.com',
            '<API_KEY>',
            '<DATABASE_HOST>',
            '<USERNAME>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/supabase/report',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(
            sent,
            {
                'endpoint',
                'apiKey',
                'databaseHost',
                'username',
                'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get(
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/<MIGRATION_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_retry(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.retry(
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/<MIGRATION_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
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
        response = self.migrations.delete(
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/<MIGRATION_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)
