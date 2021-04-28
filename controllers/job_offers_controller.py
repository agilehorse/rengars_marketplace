import connexion

from App import db
from models.CreateJobOfferDto import CreateJobOfferDto
from models.JobOffer import JobOffer  # noqa: E501
from models.RestException import RestException
from services.JobApplicationService import JobApplicationService
from services.JobOfferService import JobOfferService
from utils.utils import remap_id, get_error_dto


def create_job_offer():  # noqa: E501
    """Creates a Job offer.

     # noqa: E501

    :rtype: JobOffer
    """
    dto = CreateJobOfferDto.from_dict(connexion.request.json)
    try:
        json = JobOfferService.create_job_offer(dto)
        return remap_id(json), 200
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
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
    search_id_query = {"_id": id}
    try:
        job_offer = JobOfferService.find_job_offer(search_id_query)

        if includeApplications:
            job_applications_query = {"jobOfferId": id}
            job_offer['applications'] = JobApplicationService.find_job_applications(job_applications_query)
        return job_offer, 200
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
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

    :param id:
    :type id: int

    :rtype: None
    """
    search_query = {"_id": id}
    try:
        new_state = connexion.request.json.get('state')
        JobOfferService.update_job_offer(search_query, new_state)
        return None, 200
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_offers.unknown")
