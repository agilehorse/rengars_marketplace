from App import application
from apptest import BaseTestCase
from models.CreateJobOfferDto import CreateJobOfferDto
from models.JobOfferState import JobOfferState
from models.RestException import RestException
from services.JobOfferService import JobOfferService
from services.TestDataGenerator import TestDataGenerator
from utils.utils import get_next_id


class JobOfferServiceTest(BaseTestCase):

    def test_find_job_offer(self):
        unknown_id = 5
        query = {"_id": unknown_id}
        with self.assertRaises(RestException):
            JobOfferService.find_job_offer(query)

    def test_update_job_offer(self):
        job_offer = TestDataGenerator.get_job_offer()
        job_offer_id = job_offer['_id'] = get_next_id('offerId')
        job_offer['state'] = JobOfferState.OPEN
        application.db.job_offers.insert_one(job_offer)

        query = {'_id': job_offer_id}
        new_state = JobOfferState.COMPLETED
        JobOfferService.update_job_offer(query, new_state)

        updated = application.db.job_offers.find_one(query)
        self.assertEqual(new_state, updated['state'])

    def test_2(self):
        dto = CreateJobOfferDto.from_dict(TestDataGenerator.get_create_job_offer_dto())
        offer = JobOfferService.create_job_offer(dto)
        self.assertEqual(dto.poster_id, offer['poster']['id'])
        self.assertEqual(dto.description, offer['description'])
        self.assertEqual(dto.position_name, offer['positionName'])
        self.assertEqual(dto.company_name, offer['companyName'])

    def setUp(self) -> None:
        application.db.job_offers.delete_many({})


if __name__ == '__main__':
    import unittest

    unittest.main()
