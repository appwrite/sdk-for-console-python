import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.console import Console

class ConsoleServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.console = Console(self.client)

    @requests_mock.Mocker()
    def test_get_campaign(self, m):
        data = {
    "$id": "",
    "template": "",
    "title": "",
    "description": ""
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.get_campaign(
            '<CAMPAIGN_ID>',
        )

        self.assertEqual(response.to_dict(), data)

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

        response = self.console.get_coupon(
            '<COUPON_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_databases(self, m):
        data = {
    "total": 5.0,
    "databases": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.list_databases(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_o_auth2_providers(self, m):
        data = {
    "total": 5.0,
    "oAuth2Providers": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.list_o_auth2_providers(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_plans(self, m):
        data = {
    "total": 5.0,
    "plans": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.get_plans(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_plan(self, m):
        data = {
    "$id": "tier-0",
    "name": "Hobby",
    "desc": "Hobby plan",
    "order": 0.0,
    "price": 25,
    "trial": 14.0,
    "bandwidth": 25.0,
    "storage": 25.0,
    "imageTransformations": 100.0,
    "screenshotsGenerated": 50.0,
    "webhooks": 25.0,
    "wafRules": 2.0,
    "projects": 2.0,
    "platforms": 3.0,
    "users": 25.0,
    "teams": 25.0,
    "databases": 25.0,
    "databasesReads": 500000.0,
    "databasesWrites": 250000.0,
    "databasesBatchSize": 100.0,
    "buckets": 25.0,
    "fileSize": 25.0,
    "functions": 25.0,
    "sites": 1.0,
    "executions": 25.0,
    "executionsRetentionCount": 10000.0,
    "GBHours": 100.0,
    "realtime": 25.0,
    "realtimeMessages": 100000.0,
    "messages": 1000.0,
    "topics": 1.0,
    "authPhone": 10.0,
    "domains": 5.0,
    "usageLogs": 30.0,
    "projectInactivityDays": 7.0,
    "alertLimit": 80.0,
    "usage": {
        "bandwidth": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "executions": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "realtime": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "realtimeMessages": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "storage": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "users": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "GBHours": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        },
        "imageTransformations": {
            "name": "",
            "unit": "GB",
            "currency": "USD",
            "price": 5,
            "value": 25.0,
            "invoiceDesc": ""
        }
    },
    "addons": {},
    "budgetCapEnabled": True,
    "customSmtp": True,
    "emailBranding": True,
    "requiresPaymentMethod": True,
    "requiresBillingAddress": True,
    "isAvailable": True,
    "selfService": True,
    "premiumSupport": True,
    "budgeting": True,
    "supportsMockNumbers": True,
    "supportsOrganizationRoles": True,
    "supportsCredits": True,
    "supportsDisposableEmailValidation": True,
    "supportsCanonicalEmailValidation": True,
    "supportsFreeEmailValidation": True,
    "supportsCorporateEmailValidation": True,
    "supportsProjectSpecificRoles": True,
    "usagePerProject": True,
    "supportedAddons": {
        "baa": True,
        "premiumGeoDB": True,
        "premiumGeoDBOrg": True
    },
    "deploymentSize": 30.0,
    "buildSize": 2000.0,
    "databasesAllowEncrypt": True,
    "group": "pro"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.get_plan(
            '<PLAN_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_postgres_extensions(self, m):
        data = {
    "total": 5.0,
    "extensions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.list_postgres_extensions(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_program(self, m):
        data = {
    "$id": "",
    "title": "",
    "description": "",
    "tag": "",
    "icon": "",
    "url": "",
    "active": True,
    "external": True,
    "billingPlanId": ""
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.get_program(
            '<PROGRAM_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_program_membership(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "VIP",
    "total": 7.0,
    "prefs": {},
    "budgetAlerts": [],
    "billingPlan": "tier-1",
    "billingPlanId": "tier-1",
    "billingPlanDetails": {
        "$id": "tier-0",
        "name": "Hobby",
        "desc": "Hobby plan",
        "order": 0.0,
        "price": 25,
        "trial": 14.0,
        "bandwidth": 25.0,
        "storage": 25.0,
        "imageTransformations": 100.0,
        "screenshotsGenerated": 50.0,
        "webhooks": 25.0,
        "wafRules": 2.0,
        "projects": 2.0,
        "platforms": 3.0,
        "users": 25.0,
        "teams": 25.0,
        "databases": 25.0,
        "databasesReads": 500000.0,
        "databasesWrites": 250000.0,
        "databasesBatchSize": 100.0,
        "buckets": 25.0,
        "fileSize": 25.0,
        "functions": 25.0,
        "sites": 1.0,
        "executions": 25.0,
        "executionsRetentionCount": 10000.0,
        "GBHours": 100.0,
        "realtime": 25.0,
        "realtimeMessages": 100000.0,
        "messages": 1000.0,
        "topics": 1.0,
        "authPhone": 10.0,
        "domains": 5.0,
        "usageLogs": 30.0,
        "projectInactivityDays": 7.0,
        "alertLimit": 80.0,
        "usage": {
            "bandwidth": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "executions": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtime": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtimeMessages": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "storage": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "users": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "GBHours": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "imageTransformations": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            }
        },
        "addons": {},
        "budgetCapEnabled": True,
        "customSmtp": True,
        "emailBranding": True,
        "requiresPaymentMethod": True,
        "requiresBillingAddress": True,
        "isAvailable": True,
        "selfService": True,
        "premiumSupport": True,
        "budgeting": True,
        "supportsMockNumbers": True,
        "supportsOrganizationRoles": True,
        "supportsCredits": True,
        "supportsDisposableEmailValidation": True,
        "supportsCanonicalEmailValidation": True,
        "supportsFreeEmailValidation": True,
        "supportsCorporateEmailValidation": True,
        "supportsProjectSpecificRoles": True,
        "usagePerProject": True,
        "supportedAddons": {
            "baa": True,
            "premiumGeoDB": True,
            "premiumGeoDBOrg": True
        },
        "deploymentSize": 30.0,
        "buildSize": 2000.0,
        "databasesAllowEncrypt": True,
        "group": "pro"
    },
    "billingEmail": "billing@org.example",
    "billingStartDate": "2020-10-15T06:38:00.000+00:00",
    "billingCurrentInvoiceDate": "2020-10-15T06:38:00.000+00:00",
    "billingNextInvoiceDate": "2020-10-15T06:38:00.000+00:00",
    "billingTrialDays": 14.0,
    "billingAggregationId": "adbc3de4rddfsd",
    "billingInvoiceId": "adbc3de4rddfsd",
    "paymentMethodId": "adbc3de4rddfsd",
    "status": "active",
    "markedForDeletion": True,
    "platform": "imagine",
    "projects": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.create_program_membership(
            '<PROGRAM_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_regions(self, m):
        data = {
    "total": 5.0,
    "regions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.list_regions(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_resource(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.get_resource(
            '<VALUE>',
            'rules',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_organization_scopes(self, m):
        data = {
    "total": 5.0,
    "scopes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.list_organization_scopes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_project_scopes(self, m):
        data = {
    "total": 5.0,
    "scopes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.list_project_scopes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_source(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.create_source(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_suggest_columns(self, m):
        data = {
    "total": 5.0,
    "columns": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.suggest_columns(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_suggest_indexes(self, m):
        data = {
    "total": 5.0,
    "indexes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.suggest_indexes(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_suggest_queries(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.suggest_queries(
            'activities',
            '<INPUT>',
        )

        self.assertEqual(response, data)

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
    "subject": "Please verify your email address"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.get_email_template(
            'verification',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_variables(self, m):
        data = {
    "_APP_DOMAIN_TARGET_CNAME": "appwrite.io",
    "_APP_DOMAIN_TARGET_A": "127.0.0.1",
    "_APP_COMPUTE_BUILD_TIMEOUT": 900.0,
    "_APP_DOMAIN_TARGET_AAAA": "::1",
    "_APP_DOMAIN_TARGET_CAA": "digicert.com",
    "_APP_STORAGE_LIMIT": 30000000.0,
    "_APP_COMPUTE_SIZE_LIMIT": 30000000.0,
    "_APP_USAGE_STATS": "enabled",
    "_APP_VCS_ENABLED": True,
    "_APP_VCS_PROVIDERS": [],
    "_APP_DOMAIN_ENABLED": True,
    "_APP_ASSISTANT_ENABLED": True,
    "_APP_DOMAIN_SITES": "sites.localhost,sites.example.com",
    "_APP_DOMAIN_FUNCTIONS": "functions.localhost",
    "_APP_OPTIONS_FORCE_HTTPS": "enabled",
    "_APP_DOMAINS_NAMESERVERS": "ns1.example.com,ns2.example.com",
    "_APP_DB_ADAPTER": "mysql",
    "supportForRelationships": True,
    "supportForOperators": True,
    "supportForSpatials": True,
    "supportForSpatialIndexNull": True,
    "supportForFulltextWildcard": True,
    "supportForMultipleFulltextIndexes": True,
    "supportForAttributeResizing": True,
    "supportForSchemas": True,
    "maxIndexLength": 768.0,
    "supportForIntegerIds": True,
    "_APP_CONSOLE_EMAIL_VERIFICATION": "True"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.console.variables(
        )

        self.assertEqual(response.to_dict(), data)

