import connexion

from rengars_marketplace.models.CreateJobOfferDto import CreateJobOfferDto  # noqa: E501
from rengars_marketplace.models.JobOffer import JobOffer  # noqa: E501
from rengars_marketplace.models.UpdateJobOfferDto import UpdateJobOfferDto  # noqa: E501


def marketplace_job_offers_get():  # noqa: E501
    """Gets all Job offers.

     # noqa: E501


    :rtype: List[JobOffer]
    """
    return 'do some magic!'


def marketplace_job_offers_id_get(id, include_applications=None):  # noqa: E501
    """Gets a job offer by its id.

     # noqa: E501

    :param id: 
    :type id: int
    :param include_applications: 
    :type include_applications: bool

    :rtype: JobOffer
    """
    return 'do some magic!'


def marketplace_job_offers_id_put(body, id):  # noqa: E501
    """Updates a job offer by its id.

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateJobOfferDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def marketplace_job_offers_post(body):  # noqa: E501
    """Creates a Job offer.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: JobOffer
    """
    if connexion.request.is_json:
        body = CreateJobOfferDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
