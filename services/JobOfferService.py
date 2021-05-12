from datetime import datetime

from App import application
from models.CreateJobOfferDto import CreateJobOfferDto
from models.JobApplicationState import JobApplicationState
from models.JobOffer import JobOffer
from models.JobOfferState import JobOfferState
from models.RestException import RestException
from services.ExternalServices import ExternalServices
from utils.utils import get_next_id, remap_id


class JobOfferService:
    @staticmethod
    def find_job_offer(query: dict) -> dict:
        job_offer = application.db.job_offers.find_one(query)

        if job_offer is None:
            raise RestException("errors.job_offers.not_found", 404)
        return remap_id(job_offer)

    @staticmethod
    def update_job_offer(query: dict, new_state: str):
        job_offer = JobOfferService.find_job_offer(query)

        current_state = job_offer['state']
        if JobOfferState.is_readonly(current_state):
            raise RestException("errors.job_offers.read_only", 409, str(current_state))

        if new_state == JobOfferState.WITHDRAWN:
            accepted = list(
                application.db.job_applications.find({"jobOfferId": id, "state": JobApplicationState.ACCEPTED}))
            if len(accepted) > 0:
                raise RestException("errors.job_offers.withdrawing_accepted", 409)

        update_object = {"state": new_state}
        if JobOfferState.is_readonly(new_state):
            applications_query = {"jobOfferId": id, "$in": ["NEW, ACTIVE"]}
            application.db.job_applications.update_many(applications_query,
                                                        {'$set': {'state': JobApplicationState.REJECTED}})
            update_object['dateClosed'] = datetime.now()

        application.db.job_offers.update_one(query, {'$set': update_object})
        # todo send event to other microservices

    @staticmethod
    def create_job_offer(dto: CreateJobOfferDto) -> dict:
        job_offer = JobOffer.from_dto(dto)
        job_offer.poster = ExternalServices.get_user_info(dto.poster_id)
        job_offer.state = JobOfferState.OPEN
        job_offer.date_created = datetime.now()

        json = job_offer.to_dict()
        json['_id'] = get_next_id("offerId")
        application.db.job_offers.insert_one(json)
        # todo send event to other microservices
        return remap_id(json)

    @staticmethod
    def find_job_offers():
        job_applications = list(application.db.job_applications.find())
        # we need to remap mongodb '_id' to 'id'
        return list(map(remap_id, job_applications))
