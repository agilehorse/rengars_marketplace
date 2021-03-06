from datetime import datetime

from App import application
from models.CreateJobApplicationDto import CreateJobApplicationDto
from models.JobApplication import JobApplication
from models.JobApplicationState import JobApplicationState
from models.RestException import RestException
from services.ExternalServices import ExternalServices
from utils.utils import get_next_id, remap_id


class JobApplicationService:
    @staticmethod
    def find_job_application(query: dict) -> dict:
        job_application = application.db.job_applications.find_one(query)

        if job_application is None:
            raise RestException("errors.job_applications.not_found", 404)
        return remap_id(job_application)

    @staticmethod
    def update_job_application(query: dict, update_object: dict):
        job_application = JobApplicationService.find_job_application(query)

        current_state = job_application['state']
        if JobApplicationState.is_readonly(current_state):
            raise RestException("errors.job_applications.read_only", 409, str(current_state))

        application.db.job_applications.update_one(query, {'$set': update_object})

    @staticmethod
    def create_job_application(dto: CreateJobApplicationDto) -> dict:
        offer = application.db.job_offers.find_one({'_id': dto.job_offer_id})
        if offer is None:
            raise RestException("errors.job_offers.not_found", 404)

        job_application = JobApplication.from_dto(dto)
        job_application.state = JobApplicationState.NEW
        job_application.date_created = datetime.now()
        job_application.applicant = ExternalServices.get_user_info(dto.applicant_id)

        json = job_application.to_dict()
        json['_id'] = get_next_id("applicationId")
        application.db.job_applications.insert_one(json)
        return remap_id(json)

    @staticmethod
    def find_job_applications(query=None):
        if query is None:
            query = {}
        job_applications = list(application.db.job_applications.find(query))
        # we need to remap mongodb '_id' to 'id'
        return list(map(remap_id, job_applications))
