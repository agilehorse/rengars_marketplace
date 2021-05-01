from App import application
from models.CreateJobApplicationDto import CreateJobApplicationDto
from models.JobApplicationState import JobApplicationState
from models.RestException import RestException
from services.JobApplicationService import JobApplicationService
from services.TestDataGenerator import TestDataGenerator
from test import BaseTestCase
from utils.utils import get_next_id


class JobApplicationServiceTest(BaseTestCase):

    def test_find_job_application(self):
        unknown_id = 5
        query = {"_id": unknown_id}
        with self.assertRaises(RestException):
            JobApplicationService.find_job_application(query)

    def test_update_job_application(self):
        job_application = TestDataGenerator.get_job_application()
        job_application_id = job_application['_id'] = get_next_id('applicationId')
        job_application['state'] = JobApplicationState.NEW
        application.db.job_applications.insert_one(job_application)

        query = {"_id": job_application_id}
        new_state = JobApplicationState.ACCEPTED
        JobApplicationService.update_job_application(query, {'state': new_state})

        actual = application.db.job_applications.find_one(query)
        self.assertEqual(new_state, actual['state'])

    def test_create_job_application(self):
        job_offer = TestDataGenerator.get_job_offer()
        job_offer_id = job_offer['_id'] = job_offer.pop('id')
        application.db.job_offers.insert_one(job_offer)
        expected = CreateJobApplicationDto.from_dict(TestDataGenerator.get_create_job_application_dto(job_offer_id))

        actual = JobApplicationService.create_job_application(expected)

        self.assertEqual(expected.job_offer_id, actual['jobOfferId'])
        self.assertEqual(expected.applicant_id, actual['applicant']['id'])
        self.assertEqual(expected.note, actual['note'])

    def setUp(self) -> None:
        application.db.job_applications.delete_many({})


if __name__ == '__main__':
    import unittest

    unittest.main()
