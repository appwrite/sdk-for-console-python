import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.waf import Waf


class WafServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.waf = Waf(self.client)

    @requests_mock.Mocker()
    def test_list_rules(self, m):
        data = {
            "total": 5.0,
            "rules": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.list_rules()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_bypass_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_bypass_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/bypass',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'ruleId',
                'resourceType',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_bypass_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_bypass_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/bypass/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_challenge_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "challengeType": "compute",
            "difficulty": 3.0,
            "ttl": 1800.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_challenge_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/challenge',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'ruleId',
                'resourceType',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_challenge_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "challengeType": "compute",
            "difficulty": 3.0,
            "ttl": 1800.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_challenge_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/challenge/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_deny_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_deny_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/deny',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'ruleId',
                'resourceType',
                'name',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_deny_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/deny/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_rate_limit_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "limit": 1000.0,
            "interval": 60.0,
            "key": "userId",
            "strategy": "slidingWindow",
            "maxBucketSize": 200.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_rate_limit_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            1,
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/rate-limit',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'ruleId',
                'resourceType',
                'name',
                'limit',
                'interval',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_rate_limit_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "limit": 1000.0,
            "interval": 60.0,
            "key": "userId",
            "strategy": "slidingWindow",
            "maxBucketSize": 200.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_rate_limit_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/rate-limit/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_redirect_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "location": "\/maintenance",
            "statusCode": 301.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_redirect_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            '<LOCATION>',
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/redirect',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(
            sent,
            {
                'ruleId',
                'resourceType',
                'name',
                'location',
                'statusCode',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_redirect_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "location": "\/maintenance",
            "statusCode": 301.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_redirect_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/redirect/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.get_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/<RULE_ID>',
        )
        sent = {re.sub(r'\[.*', '', key) for key in parse_qs(url.query, keep_blank_values=True)}
        self.assertEqual(sent, set())
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_rule(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.delete_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/<RULE_ID>',
        )
        sent = set(json.loads(request.body or '{}'))
        self.assertEqual(sent, set())
        self.assertEqual(response, data)
