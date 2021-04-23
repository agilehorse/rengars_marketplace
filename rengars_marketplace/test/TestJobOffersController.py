# coding: utf-8

from __future__ import absolute_import

from flask import json

from rengars_marketplace.models.CreateJobOfferDto import CreateJobOfferDto  # noqa: E501
from rengars_marketplace.models.UpdateJobOfferDto import UpdateJobOfferDto  # noqa: E501
from rengars_marketplace.test import BaseTestCase


class TestJobOffersController(BaseTestCase):
    """JobOffersController integration test stubs"""

    def test_marketplace_job_offers_get(self):
        """Test case for marketplace_job_offers_get

        Gets all Job offers.
        """
        response = self.client.open(
            '/marketplace/jobOffers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_offers_id_get(self):
        """Test case for marketplace_job_offers_id_get

        Gets a job offer by its id.
        """
        query_string = [('include_applications', True)]
        response = self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_offers_id_put(self):
        """Test case for marketplace_job_offers_id_put

        Updates a job offer by its id.
        """
        body = UpdateJobOfferDto()
        response = self.client.open(
            '/marketplace/jobOffers/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_offers_post(self):
        """Test case for marketplace_job_offers_post

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


if __name__ == '__main__':
    import unittest
    unittest.main()
