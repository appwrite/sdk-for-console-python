import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.account import Account

class AccountServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.account = Account(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
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

        response = self.account.get(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
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

        response = self.account.create(
            '<USER_ID>',
            'email@example.com',
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_billing_addresses(self, m):
        data = {
    "total": 5.0,
    "billingAddresses": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_billing_addresses(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_billing_address(self, m):
        data = {
    "$id": "eu-fr",
    "userId": "5e5ea5c16897e",
    "streetAddress": "13th Avenue",
    "addressLine2": "",
    "country": "USA",
    "city": "",
    "state": "",
    "postalCode": ""
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_billing_address(
            '<COUNTRY>',
            '<CITY>',
            '<STREET_ADDRESS>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_billing_address(self, m):
        data = {
    "$id": "eu-fr",
    "userId": "5e5ea5c16897e",
    "streetAddress": "13th Avenue",
    "addressLine2": "",
    "country": "USA",
    "city": "",
    "state": "",
    "postalCode": ""
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_billing_address(
            '<BILLING_ADDRESS_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_billing_address(self, m):
        data = {
    "$id": "eu-fr",
    "userId": "5e5ea5c16897e",
    "streetAddress": "13th Avenue",
    "addressLine2": "",
    "country": "USA",
    "city": "",
    "state": "",
    "postalCode": ""
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_billing_address(
            '<BILLING_ADDRESS_ID>',
            '<COUNTRY>',
            '<CITY>',
            '<STREET_ADDRESS>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_billing_address(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_billing_address(
            '<BILLING_ADDRESS_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_consents(self, m):
        data = {
    "total": 5.0,
    "consents": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_consents(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_consent(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c16897e",
    "appId": "5e5ea5c16897e",
    "cimdUrl": "https:\/\/example.com\/.well-known\/client-metadata.json",
    "scopes": [],
    "resources": [],
    "authorizationDetails": "[{\"type\":\"calendar\",\"identifier\":\"primary\",\"actions\":[\"read_events\",\"create_event\"]}]",
    "expire": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_consent(
            '<CONSENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_consent(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_consent(
            '<CONSENT_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_consent_tokens(self, m):
        data = {
    "total": 5.0,
    "tokens": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_consent_tokens(
            '<CONSENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_consent_token(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "consentId": "5e5ea5c16897e",
    "userId": "5e5ea5c16897e",
    "appId": "5e5ea5c16897e",
    "cimdUrl": "https:\/\/example.com\/.well-known\/client-metadata.json",
    "scopes": [],
    "resources": [],
    "authorizationDetails": "[{\"type\":\"calendar\",\"identifier\":\"primary\",\"actions\":[\"read_events\",\"create_event\"]}]",
    "expire": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_consent_token(
            '<CONSENT_ID>',
            '<TOKEN_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_consent_token(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_consent_token(
            '<CONSENT_ID>',
            '<TOKEN_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_coupon(self, m):
        data = {
    "$id": "NEWBONUS",
    "code": "NEWBONUS",
    "credits": 50,
    "expiration": "2020-10-15T06:38:00.000+00:00",
    "validity": 180.0,
    "campaign": "AppwriteHeroes",
    "status": "disabled",
    "onlyNewOrgs": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_coupon(
            '<COUPON_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email(self, m):
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

        response = self.account.update_email(
            'email@example.com',
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_identities(self, m):
        data = {
    "total": 5.0,
    "identities": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_identities(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_identity(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_identity(
            '<IDENTITY_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_invoices(self, m):
        data = {
    "total": 5.0,
    "invoices": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_invoices(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_jwt(self, m):
        data = {
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_jwt(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_keys(self, m):
        data = {
    "total": 5.0,
    "keys": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_keys(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_key(
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_key(
            '<KEY_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_key(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_key(
            '<KEY_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_logs(self, m):
        data = {
    "total": 5.0,
    "logs": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_logs(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa(self, m):
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

        response = self.account.update_mfa(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_authenticator(self, m):
        data = {
    "secret": "[SHARED_SECRET]",
    "uri": "otpauth:\/\/totp\/appwrite:user@example.com?secret=[SHARED_SECRET]&issuer=appwrite"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_mfa_authenticator(
            'totp',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_authenticator(self, m):
        data = {
    "secret": "[SHARED_SECRET]",
    "uri": "otpauth:\/\/totp\/appwrite:user@example.com?secret=[SHARED_SECRET]&issuer=appwrite"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_mfa_authenticator(
            'totp',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_authenticator(self, m):
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

        response = self.account.update_mfa_authenticator(
            'totp',
            '<OTP>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_authenticator(self, m):
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

        response = self.account.update_mfa_authenticator(
            'totp',
            '<OTP>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_mfa_authenticator(
            'totp',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_mfa_authenticator(
            'totp',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_mfa_challenge(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "expire": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_mfa_challenge(
            'email',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_challenge(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "expire": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_mfa_challenge(
            'email',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_challenge(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_mfa_challenge(
            '<CHALLENGE_ID>',
            '<OTP>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_challenge(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_mfa_challenge(
            '<CHALLENGE_ID>',
            '<OTP>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mfa_factors(self, m):
        data = {
    "totp": True,
    "phone": True,
    "email": True,
    "recoveryCode": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_mfa_factors(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mfa_factors(self, m):
        data = {
    "totp": True,
    "phone": True,
    "email": True,
    "recoveryCode": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_mfa_factors(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_mfa_recovery_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_mfa_recovery_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_mfa_recovery_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_mfa_recovery_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_mfa_recovery_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_mfa_recovery_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_name(self, m):
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

        response = self.account.update_name(
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password(self, m):
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

        response = self.account.update_password(
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_payment_methods(self, m):
        data = {
    "total": 5.0,
    "paymentMethods": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_payment_methods(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_payment_method(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "providerMethodId": "abdk3ed3sdkfj",
    "clientSecret": "seti_ddfe",
    "providerUserId": "abdk3ed3sdkfj",
    "userId": "5e5ea5c16897e",
    "expiryMonth": 2.0,
    "expiryYear": 2024.0,
    "last4": "4242",
    "brand": "visa",
    "name": "John Doe",
    "mandateId": "yxc",
    "country": "de",
    "state": "",
    "lastError": "Your card has insufficient funds.",
    "default": True,
    "expired": True,
    "failed": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_payment_method(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_payment_method(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "providerMethodId": "abdk3ed3sdkfj",
    "clientSecret": "seti_ddfe",
    "providerUserId": "abdk3ed3sdkfj",
    "userId": "5e5ea5c16897e",
    "expiryMonth": 2.0,
    "expiryYear": 2024.0,
    "last4": "4242",
    "brand": "visa",
    "name": "John Doe",
    "mandateId": "yxc",
    "country": "de",
    "state": "",
    "lastError": "Your card has insufficient funds.",
    "default": True,
    "expired": True,
    "failed": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_payment_method(
            '<PAYMENT_METHOD_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_payment_method(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "providerMethodId": "abdk3ed3sdkfj",
    "clientSecret": "seti_ddfe",
    "providerUserId": "abdk3ed3sdkfj",
    "userId": "5e5ea5c16897e",
    "expiryMonth": 2.0,
    "expiryYear": 2024.0,
    "last4": "4242",
    "brand": "visa",
    "name": "John Doe",
    "mandateId": "yxc",
    "country": "de",
    "state": "",
    "lastError": "Your card has insufficient funds.",
    "default": True,
    "expired": True,
    "failed": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_payment_method(
            '<PAYMENT_METHOD_ID>',
            1,
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_payment_method(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_payment_method(
            '<PAYMENT_METHOD_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_payment_method_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "providerMethodId": "abdk3ed3sdkfj",
    "clientSecret": "seti_ddfe",
    "providerUserId": "abdk3ed3sdkfj",
    "userId": "5e5ea5c16897e",
    "expiryMonth": 2.0,
    "expiryYear": 2024.0,
    "last4": "4242",
    "brand": "visa",
    "name": "John Doe",
    "mandateId": "yxc",
    "country": "de",
    "state": "",
    "lastError": "Your card has insufficient funds.",
    "default": True,
    "expired": True,
    "failed": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_payment_method_provider(
            '<PAYMENT_METHOD_ID>',
            '<PROVIDER_METHOD_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_payment_method_mandate_options(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "providerMethodId": "abdk3ed3sdkfj",
    "clientSecret": "seti_ddfe",
    "providerUserId": "abdk3ed3sdkfj",
    "userId": "5e5ea5c16897e",
    "expiryMonth": 2.0,
    "expiryYear": 2024.0,
    "last4": "4242",
    "brand": "visa",
    "name": "John Doe",
    "mandateId": "yxc",
    "country": "de",
    "state": "",
    "lastError": "Your card has insufficient funds.",
    "default": True,
    "expired": True,
    "failed": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_payment_method_mandate_options(
            '<PAYMENT_METHOD_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_phone(self, m):
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

        response = self.account.update_phone(
            '+12065550100',
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_prefs(
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_prefs(self, m):
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

        response = self.account.update_prefs(
            {},
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_recovery(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_recovery(
            'email@example.com',
            'https://example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_recovery(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_recovery(
            '<USER_ID>',
            '<SECRET>',
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_sessions(self, m):
        data = {
    "total": 5.0,
    "sessions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.list_sessions(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_sessions(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_sessions(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_anonymous_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_anonymous_session(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_password_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_email_password_session(
            'email@example.com',
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_magic_url_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_magic_url_session(
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_o_auth2_session(self, m):
        data = None
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_o_auth2_session(
            'amazon',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_phone_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_phone_session(
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_session(
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.get_session(
            '<SESSION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5bb8c16897e",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "provider": "email",
    "providerUid": "user@example.com",
    "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
    "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "ip": "127.0.0.1",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States",
    "current": True,
    "factors": [],
    "secret": "5e5bb8c16897e",
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_session(
            '<SESSION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_session(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_session(
            '<SESSION_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_status(self, m):
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

        response = self.account.update_status(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_push_target(self, m):
        data = {
    "$id": "259125845563242502",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Apple iPhone 12",
    "userId": "259125845563242502",
    "providerType": "email",
    "identifier": "token",
    "expired": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_push_target(
            '<TARGET_ID>',
            '<IDENTIFIER>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_push_target(self, m):
        data = {
    "$id": "259125845563242502",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Apple iPhone 12",
    "userId": "259125845563242502",
    "providerType": "email",
    "identifier": "token",
    "expired": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_push_target(
            '<TARGET_ID>',
            '<IDENTIFIER>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_push_target(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.delete_push_target(
            '<TARGET_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_email_token(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_email_token(
            '<USER_ID>',
            'email@example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_magic_url_token(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_magic_url_token(
            '<USER_ID>',
            'email@example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_o_auth2_token(self, m):
        data = None
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_o_auth2_token(
            'amazon',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_phone_token(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_phone_token(
            '<USER_ID>',
            '+12065550100',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_verification(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_email_verification(
            'https://example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_verification(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_verification(
            'https://example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_verification(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_email_verification(
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_verification(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_verification(
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_phone_verification(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.create_phone_verification(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_phone_verification(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.account.update_phone_verification(
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

