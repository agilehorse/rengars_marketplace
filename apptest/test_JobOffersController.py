# coding: utf-8

from __future__ import absolute_import

from unittest.mock import patch

from flask import json

from App import application
from apptest import BaseTestCase
from models.JobOfferState import JobOfferState
from services.TestDataGenerator import TestDataGenerator
from utils.utils import get_next_id


class TestJobOffersController(BaseTestCase):
    """JobOffersController integration tests stubs"""

    @patch('services.ExternalServices.ExternalServices.call_eureka')
    def test_create_job_offer(self, eureka_mock):
        """Test case for create_job_offer

        Creates a Job offer.
        """
        body = TestDataGenerator.get_create_job_offer_dto()
        eureka_mock.return_value = {"id": body['posterId']}
        response = self.client.open(
            '/marketplace/jobOffers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        response_string = response.data.decode('utf-8')
        self.assert200(response, 'Response body is : ' + response_string)
        response_object = json.loads(response_string)

        self.assertEqual(body["companyName"], response_object["companyName"])
        self.assertEqual(body["description"], response_object["description"])
        self.assertEqual(body["positionName"], response_object["positionName"])
        self.assertEqual(body["posterId"], response_object["poster"]["id"])

    def test_get_job_offer(self):
        """Test case for get_job_offer

        Gets a job offer by its id.
        """
        test_job_offer = TestDataGenerator.get_job_offer()
        offer_id = test_job_offer['_id'] = get_next_id('offerId')
        application.db.job_offers.insert_one(test_job_offer)

        response = self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=offer_id),
            method='GET')
        response_string = response.data.decode('utf-8')
        self.assert200(response, 'Response body is : ' + response_string)
        response_object = json.loads(response_string)

        self.assertEqual(test_job_offer["companyName"], response_object["companyName"])
        self.assertEqual(test_job_offer["description"], response_object["description"])
        self.assertEqual(test_job_offer["positionName"], response_object["positionName"])
        self.assertEqual(test_job_offer["poster"]["id"], response_object["poster"]["id"])
        self.assertEqual(test_job_offer["_id"], response_object["id"])

    def test_update_job_offer(self):
        """Test case for update_job_offer

        Updates a job offer by its id.
        """
        test_job_offer = TestDataGenerator.get_job_offer()
        offer_id = test_job_offer['_id'] = get_next_id('offerId')
        test_job_offer['state'] = JobOfferState.OPEN
        application.db.job_offers.insert_one(test_job_offer)
        body = {"state": JobOfferState.WITHDRAWN}

        response = self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=offer_id),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

        response_object = json.loads(self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=offer_id),
            method='GET').data.decode('utf-8'))

        self.assertEqual(body["state"], response_object["state"])

    def setUp(self) -> None:
        application.db.job_offers.delete_many({})


if __name__ == '__main__':
    import unittest

    unittest.main()
