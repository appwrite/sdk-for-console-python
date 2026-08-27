import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.domains import Domains


class DomainsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.domains = Domains(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "domains": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.list()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create(
            '<TEAM_ID>',
            '',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_price(self, m):
        data = {
            "domain": "example.com",
            "tld": "com",
            "available": True,
            "price": 25.99,
            "periodYears": 1.0,
            "premium": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_price(
            '',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_purchase(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domainId": "5e5ea5c16897e",
            "domain": "example.com",
            "organizationId": "5e5ea5c16897e",
            "status": "pending",
            "clientSecret": "",
            "amount": 25.99,
            "currency": "USD",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_purchase(
            '',
            '<ORGANIZATION_ID>',
            '<FIRST_NAME>',
            '<LAST_NAME>',
            'email@example.com',
            '+12065550100',
            '<BILLING_ADDRESS_ID>',
            '<PAYMENT_METHOD_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_purchase(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domainId": "5e5ea5c16897e",
            "domain": "example.com",
            "organizationId": "5e5ea5c16897e",
            "status": "pending",
            "clientSecret": "",
            "amount": 25.99,
            "currency": "USD",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_purchase(
            '<INVOICE_ID>',
            '<ORGANIZATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_suggestions(self, m):
        data = {
            "total": 5.0,
            "suggestions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.list_suggestions(
            '<QUERY>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_transfer_in(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domainId": "5e5ea5c16897e",
            "domain": "example.com",
            "organizationId": "5e5ea5c16897e",
            "status": "pending",
            "clientSecret": "",
            "amount": 25.99,
            "currency": "USD",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_transfer_in(
            '',
            '<ORGANIZATION_ID>',
            '<AUTH_CODE>',
            '<PAYMENT_METHOD_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_transfer_in(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domainId": "5e5ea5c16897e",
            "domain": "example.com",
            "organizationId": "5e5ea5c16897e",
            "status": "pending",
            "clientSecret": "",
            "amount": 25.99,
            "currency": "USD",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_transfer_in(
            '<INVOICE_ID>',
            '<ORGANIZATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_transfer_out(self, m):
        data = {
            "authCode": "mock_1a2b3c4d",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_transfer_out(
            '<DOMAIN_ID>',
            '<ORGANIZATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get(
            '<DOMAIN_ID>',
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
        response = self.domains.delete(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_auto_renewal(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_auto_renewal(
            '<DOMAIN_ID>',
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_nameservers(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_nameservers(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_verify_nameservers(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.verify_nameservers(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_google_workspace(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_google_workspace(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_google_workspace(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_google_workspace(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_i_cloud(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_i_cloud(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_i_cloud(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_i_cloud(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_mailgun(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_mailgun(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_mailgun(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_mailgun(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_outlook(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_outlook(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_outlook(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_outlook(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_proton_mail(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_proton_mail(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_proton_mail(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_proton_mail(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_zoho(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_zoho(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_zoho(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_zoho(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_records(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.list_records(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_a(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_a(
            '<DOMAIN_ID>',
            '',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_a(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_a(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_aaaa(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_aaaa(
            '<DOMAIN_ID>',
            '',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_aaaa(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_aaaa(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_alias(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_alias(
            '<DOMAIN_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_alias(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_alias(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_caa(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_caa(
            '<DOMAIN_ID>',
            '',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_caa(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_caa(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_cname(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_cname(
            '<DOMAIN_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_cname(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_cname(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_https(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_https(
            '<DOMAIN_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_https(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_https(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_mx(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_mx(
            '<DOMAIN_ID>',
            '',
            '<VALUE>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_mx(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_mx(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_ns(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_ns(
            '<DOMAIN_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_ns(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_ns(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_srv(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_srv(
            '<DOMAIN_ID>',
            '',
            '<VALUE>',
            1,
            1,
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_srv(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_srv(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
            1,
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_txt(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_txt(
            '<DOMAIN_ID>',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_txt(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_txt(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            '',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_record(self, m):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_record(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_record(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.delete_record(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_team(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_team(
            '<DOMAIN_ID>',
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_transfer_status(self, m):
        data = {
            "status": "pending_registry",
            "reason": "Transfer in progress",
            "timestamp": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_transfer_status(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_zone(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_zone(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_zone(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_zone(
            '<DOMAIN_ID>',
            '<CONTENT>',
        )
        self.assertEqual(response.to_dict(), data)
