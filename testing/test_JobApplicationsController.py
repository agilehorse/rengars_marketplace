# coding: utf-8
import json
from unittest.mock import patch

from App import application
from models.JobApplicationState import JobApplicationState
from services.TestDataGenerator import TestDataGenerator
from testing import BaseTestCase
from utils.utils import get_next_id


class TestJobApplicationsController(BaseTestCase):
    """ApplicationsController integration tests stubs"""

    def test_change_job_application_state(self):
        """Test case for change_job_application_state

        Changes a state of a job application by its id.
        """
        test_job_application = TestDataGenerator.get_job_application()
        application_id = test_job_application['_id'] = get_next_id('applicationId')
        application.db.job_applications.insert_one(test_job_application)

        body = {'state': JobApplicationState.ACTIVE}
        response = self.client.open(
            '/marketplace/jobApplications/{id}/changeState'.format(id=application_id),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

        response_body = json.loads(self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=application_id),
            method='GET').data.decode('utf-8'))
        self.assertEqual(response_body['state'], body['state'])

    def test_create_job_application(self):
        """Test case for create_job_application

        Creates a job application.
        """
        body = TestDataGenerator.get_create_job_application_dto()
        response = self.client.open(
            '/marketplace/jobApplications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        # 404 because job offer with the id is not present
        self.assert404(response, 'Response body is : ' + response.data.decode('utf-8'))

    @patch('App.application.db.job_applications.find_one')
    def test_get_job_application(self, mock_find):
        """Test case for get_job_application


        Gets a job application by its id.
        """
        job_application = TestDataGenerator.get_job_application()
        id = job_application['_id'] = 1
        mock_find.return_value = job_application
        response = self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=id),
            method='GET')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_update_job_application(self):
        """Test case for update_job_application

        Updates an application by its id.
        """
        test_job_application = TestDataGenerator.get_job_application()
        application_id = test_job_application['_id'] = get_next_id('applicationId')
        application.db.job_applications.insert_one(test_job_application)

        body = {'note': "Hello I have 3 years experience."}
        response = self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=application_id),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

        response_body = json.loads(self.client.open(
            '/marketplace/jobApplications/{id}'.format(id=application_id),
            method='GET').data.decode('utf-8'))
        self.assertEqual(response_body['note'], body['note'])

    def setUp(self) -> None:
        application.db.job_applications.delete_many({})


if __name__ == '__main__':
    import unittest

    unittest.main()
