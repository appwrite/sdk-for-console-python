import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.organizations import Organizations


class OrganizationsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.organizations = Organizations(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "teams": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations',
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
    def test_create(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.create(
            '<ORGANIZATION_ID>',
            '<NAME>',
            'tier-0',
            payment_method_id='<PAYMENT_METHOD_ID>',
            billing_address_id='<BILLING_ADDRESS_ID>',
            invites=[],
            coupon_id='<COUPON_ID>',
            tax_id='<TAX_ID>',
            budget=1,
            platform='appwrite',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'organizationId': '<ORGANIZATION_ID>',
                'name': '<NAME>',
                'billingPlan': 'tier-0',
                'paymentMethodId': '<PAYMENT_METHOD_ID>',
                'billingAddressId': '<BILLING_ADDRESS_ID>',
                'invites': [],
                'couponId': '<COUPON_ID>',
                'taxId': '<TAX_ID>',
                'budget': 1,
                'platform': 'appwrite',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_estimation_create_organization(self, m):
        data = {
            "amount": 50,
            "grossAmount": 50,
            "credits": 50,
            "items": [],
            "discounts": [],
            "trialDays": 14.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.estimation_create_organization(
            'tier-0',
            payment_method_id='<PAYMENT_METHOD_ID>',
            invites=[],
            coupon_id='<COUPON_ID>',
            platform='appwrite',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/estimations/create-organization',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'billingPlan': 'tier-0',
                'paymentMethodId': '<PAYMENT_METHOD_ID>',
                'invites': [],
                'couponId': '<COUPON_ID>',
                'platform': 'appwrite',
            },
        )
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
        response = self.organizations.delete(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

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
        response = self.organizations.list_addons(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_baa_addon(self, m):
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
        response = self.organizations.create_baa_addon(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons/baa',
        )
        sent = json.loads(request.body or '{}')
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
        response = self.organizations.create_premium_geo_db_addon(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons/premium-geo-db',
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
        response = self.organizations.get_addon(
            '<ORGANIZATION_ID>',
            '<ADDON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons/<ADDON_ID>',
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
        response = self.organizations.delete_addon(
            '<ORGANIZATION_ID>',
            '<ADDON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons/<ADDON_ID>',
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
        response = self.organizations.confirm_addon_payment(
            '<ORGANIZATION_ID>',
            '<ADDON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons/<ADDON_ID>/confirmations',
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
        response = self.organizations.get_addon_price(
            '<ORGANIZATION_ID>',
            'baa',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/addons/baa/price',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_aggregations(self, m):
        data = {
            "total": 5.0,
            "aggregations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.list_aggregations(
            '<ORGANIZATION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/aggregations',
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
    def test_get_aggregation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "from": "2020-10-15T06:38:00.000+00:00",
            "to": "2020-10-15T06:38:00.000+00:00",
            "usageStorage": 20009090.0,
            "usageTotalStorage": 20009090.0,
            "usageFilesStorage": 20009090.0,
            "usageDeploymentsStorage": 20009090.0,
            "usageBuildsStorage": 20009090.0,
            "usageDatabasesStorage": 2009090.0,
            "usageFunctionsStorage": 20009090.0,
            "usageSitesStorage": 20009090.0,
            "usageUsers": 2000.0,
            "usageExecutions": 2000.0,
            "usageBandwidth": 2000.0,
            "usageRealtime": 200.0,
            "usageRealtimeMessages": 10000.0,
            "usageRealtimeBandwidth": 5000000.0,
            "additionalMembers": 5.0,
            "additionalMemberAmount": 30.0,
            "additionalStorageAmount": 40.0,
            "additionalUsersAmount": 4.0,
            "additionalExecutionsAmount": 30.0,
            "additionalBandwidthAmount": 40.0,
            "additionalRealtimeAmount": 20.0,
            "plan": "tier-0",
            "amount": 2.0,
            "breakdown": [],
            "resources": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_aggregation(
            '<ORGANIZATION_ID>',
            '<AGGREGATION_ID>',
            limit=1,
            offset=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/aggregations/<AGGREGATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'limit': ['1'],
                'offset': ['1'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_set_billing_address(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.set_billing_address(
            '<ORGANIZATION_ID>',
            '<BILLING_ADDRESS_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/billing-address',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'billingAddressId': '<BILLING_ADDRESS_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_billing_address(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.delete_billing_address(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/billing-address',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_billing_address(self, m):
        data = {
            "$id": "eu-fr",
            "userId": "5e5ea5c16897e",
            "streetAddress": "13th Avenue",
            "country": "USA",
            "city": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_billing_address(
            '<ORGANIZATION_ID>',
            '<BILLING_ADDRESS_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/billing-addresses/<BILLING_ADDRESS_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_set_billing_email(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.set_billing_email(
            '<ORGANIZATION_ID>',
            'email@example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/billing-email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'billingEmail': 'email@example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_budget(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.update_budget(
            '<ORGANIZATION_ID>',
            1,
            alerts=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/budget',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'budget': 1,
                'alerts': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_credits(self, m):
        data = {
            "credits": [],
            "total": 5.0,
            "available": 5,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.list_credits(
            '<ORGANIZATION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/credits',
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
    def test_add_credit(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "couponId": "NEWBONUS",
            "userId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "credits": 50,
            "total": 50,
            "expiration": "2020-10-15T06:38:00.000+00:00",
            "status": "disabled",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.add_credit(
            '<ORGANIZATION_ID>',
            '<COUPON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/credits',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'couponId': '<COUPON_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_available_credits(self, m):
        data = {
            "available": 100.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_available_credits(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/credits/available',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_credit(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "couponId": "NEWBONUS",
            "userId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "credits": 50,
            "total": 50,
            "expiration": "2020-10-15T06:38:00.000+00:00",
            "status": "disabled",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_credit(
            '<ORGANIZATION_ID>',
            '<CREDIT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/credits/<CREDIT_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_estimation_delete_organization(self, m):
        data = {
            "unpaidInvoices": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.estimation_delete_organization(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/estimations/delete-organization',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_estimation_update_plan(self, m):
        data = {
            "amount": 50,
            "grossAmount": 50,
            "credits": 50,
            "items": [],
            "discounts": [],
            "trialDays": 14.0,
            "organizationCredits": 0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.estimation_update_plan(
            '<ORGANIZATION_ID>',
            'tier-0',
            invites=[],
            coupon_id='<COUPON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/estimations/update-plan',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'billingPlan': 'tier-0',
                'invites': [],
                'couponId': '<COUPON_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_downgrade_feedback(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "title": "I encountered a bug and outage that caused my app to lose its value",
            "message": "The platform experienced significant downtime which affected my users.",
            "fromPlanId": "pro",
            "toPlanId": "free",
            "teamId": "5e5ea5c16897e",
            "userId": "5e5ea5c16897e",
            "version": "1.8.0",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.create_downgrade_feedback(
            '<ORGANIZATION_ID>',
            '<REASON>',
            '<MESSAGE>',
            '<FROM_PLAN_ID>',
            '<TO_PLAN_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/feedbacks/downgrade',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'reason': '<REASON>',
                'message': '<MESSAGE>',
                'fromPlanId': '<FROM_PLAN_ID>',
                'toPlanId': '<TO_PLAN_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_invoices(self, m):
        data = {
            "total": 5.0,
            "invoices": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.list_invoices(
            '<ORGANIZATION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/invoices',
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
    def test_get_invoice(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "teamId": "5e5ea5c16897e",
            "aggregationId": "5e5ea5c16897e",
            "plan": "tier-1",
            "usage": [],
            "amount": 50,
            "tax": 17,
            "taxAmount": 12.5,
            "vat": 17,
            "vatAmount": 12.5,
            "grossAmount": 12.5,
            "creditsUsed": 30,
            "currency": "USD",
            "status": "succeeded",
            "type": "subscription",
            "dueAt": "2020-10-15T06:38:00.000+00:00",
            "from": "2020-10-15T06:38:00.000+00:00",
            "to": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_invoice(
            '<ORGANIZATION_ID>',
            '<INVOICE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/invoices/<INVOICE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_invoice_download(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.organizations.get_invoice_download(
            '<ORGANIZATION_ID>',
            '<INVOICE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/invoices/<INVOICE_ID>/download',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_invoice_payment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "teamId": "5e5ea5c16897e",
            "aggregationId": "5e5ea5c16897e",
            "plan": "tier-1",
            "usage": [],
            "amount": 50,
            "tax": 17,
            "taxAmount": 12.5,
            "vat": 17,
            "vatAmount": 12.5,
            "grossAmount": 12.5,
            "creditsUsed": 30,
            "currency": "USD",
            "status": "succeeded",
            "type": "subscription",
            "dueAt": "2020-10-15T06:38:00.000+00:00",
            "from": "2020-10-15T06:38:00.000+00:00",
            "to": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.create_invoice_payment(
            '<ORGANIZATION_ID>',
            '<INVOICE_ID>',
            '<PAYMENT_METHOD_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/invoices/<INVOICE_ID>/payments',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'paymentMethodId': '<PAYMENT_METHOD_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_validate_invoice(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "teamId": "5e5ea5c16897e",
            "aggregationId": "5e5ea5c16897e",
            "plan": "tier-1",
            "usage": [],
            "amount": 50,
            "tax": 17,
            "taxAmount": 12.5,
            "vat": 17,
            "vatAmount": 12.5,
            "grossAmount": 12.5,
            "creditsUsed": 30,
            "currency": "USD",
            "status": "succeeded",
            "type": "subscription",
            "dueAt": "2020-10-15T06:38:00.000+00:00",
            "from": "2020-10-15T06:38:00.000+00:00",
            "to": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.validate_invoice(
            '<ORGANIZATION_ID>',
            '<INVOICE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/invoices/<INVOICE_ID>/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_invoice_view(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.organizations.get_invoice_view(
            '<ORGANIZATION_ID>',
            '<INVOICE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/invoices/<INVOICE_ID>/view',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_set_default_payment_method(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.set_default_payment_method(
            '<ORGANIZATION_ID>',
            '<PAYMENT_METHOD_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/payment-method',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'paymentMethodId': '<PAYMENT_METHOD_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_default_payment_method(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.delete_default_payment_method(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/payment-method',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_set_backup_payment_method(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.set_backup_payment_method(
            '<ORGANIZATION_ID>',
            '<PAYMENT_METHOD_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/payment-method/backup',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'paymentMethodId': '<PAYMENT_METHOD_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_backup_payment_method(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.delete_backup_payment_method(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/payment-method/backup',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            "default": True,
            "expired": True,
            "failed": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_payment_method(
            '<ORGANIZATION_ID>',
            '<PAYMENT_METHOD_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/payment-methods/<PAYMENT_METHOD_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
            "environments": 5.0,
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
            "supportsDedicatedDatabases": True,
            "supportsDisposableEmailValidation": True,
            "supportsCanonicalEmailValidation": True,
            "supportsFreeEmailValidation": True,
            "supportsCorporateEmailValidation": True,
            "supportsProjectSpecificRoles": True,
            "usagePerProject": True,
            "supportedAddons": {
                "baa": True,
                "premiumGeoDB": True,
                "premiumGeoDBOrg": True,
            },
            "deploymentSize": 30.0,
            "buildSize": 2000.0,
            "functionsIntervalMinimum": 60.0,
            "functionsAllowCron": True,
            "databasesAllowEncrypt": True,
            "group": "pro",
            "databaseComputeCredit": 10,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_plan(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/plan',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_plan(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.update_plan(
            '<ORGANIZATION_ID>',
            'tier-0',
            payment_method_id='<PAYMENT_METHOD_ID>',
            billing_address_id='<BILLING_ADDRESS_ID>',
            invites=[],
            coupon_id='<COUPON_ID>',
            tax_id='<TAX_ID>',
            budget=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/plan',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'billingPlan': 'tier-0',
                'paymentMethodId': '<PAYMENT_METHOD_ID>',
                'billingAddressId': '<BILLING_ADDRESS_ID>',
                'invites': [],
                'couponId': '<COUPON_ID>',
                'taxId': '<TAX_ID>',
                'budget': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_plan_estimation(self, m):
        data = {
            "currentBillingPlanId": "tier-2",
            "targetBillingPlanId": "tier-0",
            "direction": "downgrade",
            "estimation": {
                "currency": "USD",
                "grossAmount": 15,
                "credits": 0,
                "organizationCredits": 5,
                "discount": 0,
                "amount": 20,
                "nextInvoiceDate": "2025-12-01T00:00:00.000Z",
                "items": [],
                "discounts": [],
            },
            "limits": {
                "canChangePlan": True,
                "unsupportedAddons": [],
                "projects": {
                    "type": "databases",
                    "currentUsage": 3.0,
                    "limit": 1.0,
                    "status": "over_limit",
                    "excess": 2.0,
                    "resolutionHint": "Delete or migrate 2 databases.",
                },
                "members": {
                    "type": "databases",
                    "currentUsage": 3.0,
                    "limit": 1.0,
                    "status": "over_limit",
                    "excess": 2.0,
                    "resolutionHint": "Delete or migrate 2 databases.",
                },
                "domains": {
                    "type": "databases",
                    "currentUsage": 3.0,
                    "limit": 1.0,
                    "status": "over_limit",
                    "excess": 2.0,
                    "resolutionHint": "Delete or migrate 2 databases.",
                },
                "nonCompliantProjects": 2.0,
                "projectCompliance": [],
            },
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.create_plan_estimation(
            '<ORGANIZATION_ID>',
            'tier-0',
            invites=[],
            coupon_id='<COUPON_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/plan/estimations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'billingPlan': 'tier-0',
                'invites': [],
                'couponId': '<COUPON_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_regions(self, m):
        data = {
            "total": 5.0,
            "regions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.list_regions(
            '<ORGANIZATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/regions',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_scopes(self, m):
        data = {
            "scopes": [],
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_scopes(
            '<ORGANIZATION_ID>',
            project_id='<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/roles',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'projectId': ['<PROJECT_ID>'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_set_billing_tax_id(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.set_billing_tax_id(
            '<ORGANIZATION_ID>',
            '<TAX_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/taxId',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'taxId': '<TAX_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_usage(self, m):
        data = {
            "bandwidth": [],
            "users": [],
            "executions": [],
            "databasesReads": [],
            "databasesWrites": [],
            "imageTransformations": [],
            "imageTransformationsTotal": 0.0,
            "screenshotsGenerated": [],
            "screenshotsGeneratedTotal": 0.0,
            "usersTotal": 0.0,
            "executionsTotal": 0.0,
            "executionsMBSecondsTotal": 0.0,
            "buildsMBSecondsTotal": 0.0,
            "filesStorageTotal": 0.0,
            "buildsStorageTotal": 0.0,
            "deploymentsStorageTotal": 0.0,
            "databasesStorageTotal": 0.0,
            "databasesReadsTotal": 0.0,
            "databasesWritesTotal": 0.0,
            "backupsStorageTotal": 0.0,
            "avatarsStorageTotal": 0.0,
            "storageTotal": 0.0,
            "authPhoneTotal": 0.0,
            "authPhoneEstimate": 0.0,
            "projects": [],
            "realtimeConnections": [],
            "realtimeConnectionsTotal": 0.0,
            "realtimeMessages": [],
            "realtimeMessagesTotal": 0.0,
            "realtimeBandwidth": [],
            "realtimeBandwidthTotal": 0.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.get_usage(
            '<ORGANIZATION_ID>',
            start_date='2020-10-15T06:38:00.000+00:00',
            end_date='2020-10-15T06:38:00.000+00:00',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/usage',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'startDate': ['2020-10-15T06:38:00.000+00:00'],
                'endDate': ['2020-10-15T06:38:00.000+00:00'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_validate_payment(self, m):
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
                "environments": 5.0,
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
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organizations.validate_payment(
            '<ORGANIZATION_ID>',
            invites=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organizations/<ORGANIZATION_ID>/validate',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'invites': [],
            },
        )
        self.assertEqual(response.to_dict(), data)
