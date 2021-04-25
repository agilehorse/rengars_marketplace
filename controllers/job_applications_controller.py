from datetime import datetime

import connexion

from App import db
from models.CreateJobApplicationDto import CreateJobApplicationDto
from models.JobApplication import JobApplication
from models.JobApplicationState import JobApplicationState  # noqa: E501
from models.User import User
from utils.utils import validate_job_application, remap_id, get_next_sequence, get_error_dto


def change_job_application_state(id: int):  # noqa: E501
    """Changes a state of a job application by its id.

     # noqa: E501

    :param id:
    :type id: int

    :rtype: None
    """
    search_id_query = {"_id": id}
    try:
        job_application = db.job_applications.find_one(search_id_query)
        if (error := validate_job_application(job_application)) is not None:
            return error

        new_state = connexion.request.json.get('state')
        update_object = {"state": new_state}
        if JobApplicationState.is_readonly(new_state):
            update_object['dateClosed'] = datetime.now()
        db.job_applications.update_one(search_id_query, {'$set': update_object})
        # todo send event to other microservices
        return None, 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")


def create_job_application():  # noqa: E501
    """Creates a job application.

     # noqa: E501

    :rtype: GetJobApplicationDto
    """
    dto = CreateJobApplicationDto.from_dict(connexion.request.json)
    offer = db.job_offers.find_one({'_id': dto.job_offer_id})
    if offer is None:
        return get_error_dto("errors.job_offers.not_found")

    job_application = JobApplication.from_dto(dto)
    job_application.state = JobApplicationState.NEW
    job_application.date_created = datetime.now()
    # job_application.applicant = todo get user info
    fake_applicant = User(dto.applicant_id, "test@email.com", datetime.now(), '+420 123 456 789')
    job_application.applicant = fake_applicant
    try:
        json = job_application.to_dict()
        json['_id'] = get_next_sequence("applicationId")
        db.job_applications.insert_one(json)
        # todo send event to other microservices
        return remap_id(json), 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")


def get_job_application(id: int):  # noqa: E501
    """Gets a job application by its id.

     # noqa: E501

    :param id:
    :type id: int

    :rtype: GetJobApplicationDto
    """
    try:
        search_id_query = {"_id": id}
        job_application = db.job_applications.find_one(search_id_query)
        if job_application is None:
            return get_error_dto("errors.job_applications.not_found")
        return remap_id(job_application), 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")


def get_job_applications():  # noqa: E501
    """Gets all Job applications.

     # noqa: E501


    :rtype: List[JobApplication]
    """
    try:
        job_applications = list(db.job_applications.find())
        return list(map(remap_id, job_applications)), 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")


def update_job_application(id: int):  # noqa: E501
    """Updates an application by its id.

     # noqa: E501

    :param id:
    :type id: int

    :rtype: None
    """
    search_id_query = {"_id": id}
    try:
        job_application = db.job_applications.find_one(search_id_query)
        if (error := validate_job_application(job_application)) is not None:
            return error

        new_note = connexion.request.json.get('note')
        db.job_applications.update_one(search_id_query, {'$set': {"note": new_note}})
        # todo send event to other microservices
        return None, 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")
