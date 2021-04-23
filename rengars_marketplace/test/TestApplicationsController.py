# coding: utf-8

from __future__ import absolute_import

from flask import json

from rengars_marketplace.models.CreateJobApplicationDto import CreateJobApplicationDto  # noqa: E501
from rengars_marketplace.models.JobApplicationStateDto import JobApplicationStateDto  # noqa: E501
from rengars_marketplace.models.UpdateJobApplicationDto import UpdateJobApplicationDto  # noqa: E501
from rengars_marketplace.test import BaseTestCase


class TestApplicationsController(BaseTestCase):
    """ApplicationsController integration test stubs"""

    def test_marketplace_job_applications_get(self):
        """Test case for marketplace_job_applications_get

        Gets all Job applications.
        """
        response = self.client.open(
            '/marketplace/jobApplications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_applications_id_change_state_put(self):
        """Test case for marketplace_job_applications_id_change_state_put

        Changes a state of a job application by its id.
        """
        body = JobApplicationStateDto()
        response = self.client.open(
            '/marketplace/jobApplications/{id}/changeState'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_applications_id_get(self):
        """Test case for marketplace_job_applications_id_get

        Gets a job application by its id.
        """
        response = self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_applications_id_put(self):
        """Test case for marketplace_job_applications_id_put

        Updates an application by its id.
        """
        body = UpdateJobApplicationDto()
        response = self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_marketplace_job_applications_post(self):
        """Test case for marketplace_job_applications_post

        Creates a job application.
        """
        body = CreateJobApplicationDto()
        response = self.client.open(
            '/marketplace/jobApplications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
