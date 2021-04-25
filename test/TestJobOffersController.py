# coding: utf-8

from __future__ import absolute_import

from flask import json

from models.CreateJobOfferDto import CreateJobOfferDto  # noqa: E501
from models.UpdateJobOfferDto import UpdateJobOfferDto  # noqa: E501
from ..test import BaseTestCase


class TestJobOffersController(BaseTestCase):
    """JobOffersController integration test stubs"""

    def test_create_job_offer(self):
        """Test case for create_job_offer

        Creates a Job offer.
        """
        body = CreateJobOfferDto()
        response = self.client.open(
            '/marketplace/jobOffers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_offer(self):
        """Test case for get_job_offer

        Gets a job offer by its id.
        """
        query_string = [('include_applications', True)]
        response = self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_offers(self):
        """Test case for get_job_offers

        Gets all Job offers.
        """
        response = self.client.open(
            '/marketplace/jobOffers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_job_offer(self):
        """Test case for update_job_offer

        Updates a job offer by its id.
        """
        body = UpdateJobOfferDto()
        response = self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
