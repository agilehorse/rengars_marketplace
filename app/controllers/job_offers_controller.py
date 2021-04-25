from datetime import datetime

import connexion
from __main__ import db
from models.JobOffer import JobOffer  # noqa: E501
from models.JobOfferState import JobOfferState

from app.models.CreateJobOfferDto import CreateJobOfferDto
from app.models.JobApplicationState import JobApplicationState
from app.models.User import User
from app.utils.utils import get_next_sequence, remap_id, validate_job_offer, get_error_dto


def create_job_offer():  # noqa: E501
    """Creates a Job offer.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes

    :rtype: JobOffer
    """
    dto = CreateJobOfferDto.from_dict(connexion.request.json)
    job_offer = JobOffer.from_dto(dto)
    # job_offer.poster = todo get user info
    fake_poster = User(dto.poster_id, "test@email.com", datetime.now(), '+420 123 456 789')
    job_offer.poster = fake_poster
    job_offer.state = JobOfferState.OPEN
    job_offer.date_created = datetime.now()
    try:
        json = job_offer.to_dict()
        json['_id'] = get_next_sequence("offerId")
        db.job_offers.insert_one(json)
        # todo send event to other microservices
        return remap_id(json), 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_offers.unknown")


def get_job_offer(id: int, includeApplications=False):  # noqa: E501
    """Gets a job offer by its id.

     # noqa: E501

    :param id:
    :type id: int
    :param includeApplications:
    :type includeApplications: bool

    :rtype: JobOffer
    """
    try:
        job_offer = db.job_offers.find_one({"_id": id})
        if job_offer is None:
            return get_error_dto("errors.job_offers.not_found")

        if includeApplications:
            job_offer['applications'] = list(map(remap_id, list(db.job_applications.find({"jobOfferId": id}))))
        return remap_id(job_offer), 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_offers.unknown")


def get_job_offers():  # noqa: E501
    """Gets all Job offers.

     # noqa: E501


    :rtype: List[JobOffer]
    """
    try:
        job_offers = list(map(remap_id, list(db.job_offers.find())))
        return job_offers, 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_offers.unknown")


def update_job_offer(id: int):  # noqa: E501
    """Updates a job offer by its id.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes
    :param id:
    :type id: int

    :rtype: None
    """
    search_query = {"_id": id}
    try:
        job_offer = db.job_offers.find_one(search_query)
        new_state = connexion.request.json.get('state')
        if (error := validate_job_offer(job_offer, new_state)) is not None:
            return error

        update_object = {"state": new_state}
        if JobOfferState.is_readonly(new_state):
            db.job_applications.update_many({"jobOfferId": id}, {'$set': {'state': JobApplicationState.REJECTED}})
            update_object['dateClosed'] = datetime.now()

        db.job_offers.update_one(search_query, {'$set': update_object})
        # todo send event to other microservices
        return None, 200
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_offers.unknown")
