import json
import requests_mock
import unittest

from appwrite_console.client import Client
from appwrite_console.input_file import InputFile
from appwrite_console.models import *
from appwrite_console.services.affiliates import Affiliates

class AffiliatesServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.affiliates = Affiliates(self.client)

    @requests_mock.Mocker()
    def test_list_links(self, m):
        data = {
    "total": 5.0,
    "links": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.list_links(
        )


        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_link(self, m):
        data = {
    "$id": "my-campaign",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c16897e",
    "name": "Launch campaign",
    "status": "active"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.create_link(
            '<LINK_ID>',
        )


        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_link(self, m):
        data = {
    "$id": "my-campaign",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c16897e",
    "name": "Launch campaign",
    "status": "active"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.get_link(
            '<LINK_ID>',
        )


        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_link(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.delete_link(
            '<LINK_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_referrals(self, m):
        data = {
    "total": 5.0,
    "referrals": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.list_referrals(
        )


        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_rewards(self, m):
        data = {
    "total": 5.0,
    "rewards": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.list_rewards(
        )


        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_reward(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c16897e",
    "linkId": "my-campaign",
    "referralId": "5e5ea5c16897e",
    "amount": 10,
    "status": "pending"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.affiliates.update_reward(
            '<REWARD_ID>',
            'claimed',
            '<ORGANIZATION_ID>',
        )


        self.assertEqual(response.to_dict(), data)

