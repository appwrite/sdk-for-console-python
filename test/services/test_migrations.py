import json
import requests_mock
import unittest

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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.list()
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
            requests_mock.ANY,
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
            requests_mock.ANY,
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_csv_export(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<FILENAME>',
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
            requests_mock.ANY,
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_firebase_migration(
            [],
            '<SERVICE_ACCOUNT>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get_firebase_report(
            [],
            '<SERVICE_ACCOUNT>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_json_export(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<FILENAME>',
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
            requests_mock.ANY,
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
            requests_mock.ANY,
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
            requests_mock.ANY,
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
            requests_mock.ANY,
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
            requests_mock.ANY,
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get(
            '<MIGRATION_ID>',
        )
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.retry(
            '<MIGRATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.delete(
            '<MIGRATION_ID>',
        )
        self.assertEqual(response, data)
