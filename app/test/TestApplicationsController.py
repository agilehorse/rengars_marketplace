# coding: utf-8

from __future__ import absolute_import

from test import BaseTestCase

from flask import json
from models.CreateJobApplicationDto import CreateJobApplicationDto  # noqa: E501
from models.JobApplicationStateDto import JobApplicationStateDto  # noqa: E501
from models.UpdateJobApplicationDto import UpdateJobApplicationDto  # noqa: E501


class TestApplicationsController(BaseTestCase):
    """ApplicationsController integration test stubs"""

    def test_change_job_application_state(self):
        """Test case for change_job_application_state

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

    def test_create_job_application(self):
        """Test case for create_job_application

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

    def test_get_job_application(self):
        """Test case for get_job_application

        Gets a job application by its id.
        """
        response = self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_applications(self):
        """Test case for get_job_applications

        Gets all Job applications.
        """
        response = self.client.open(
            '/marketplace/jobApplications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_job_application(self):
        """Test case for update_job_application

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


if __name__ == '__main__':
    import unittest

    unittest.main()
