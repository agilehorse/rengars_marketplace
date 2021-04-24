from rengars_marketplace.models.CreateJobOfferDto import CreateJobOfferDto  # noqa: E501
from rengars_marketplace.models.JobOffer import JobOffer  # noqa: E501
from rengars_marketplace.models.UpdateJobOfferDto import UpdateJobOfferDto  # noqa: E501


def create_job_offer(dto: CreateJobOfferDto):  # noqa: E501
    """Creates a Job offer.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes

    :rtype: JobOffer
    """
    return 'do some magic!'


def get_job_offer(id: int, include_applications=False):  # noqa: E501
    """Gets a job offer by its id.

     # noqa: E501

    :param id:
    :type id: int
    :param include_applications:
    :type include_applications: bool

    :rtype: JobOffer
    """
    return 'do some magic!'


def get_job_offers():  # noqa: E501
    """Gets all Job offers.

     # noqa: E501


    :rtype: List[JobOffer]
    """
    return 'do some magic!'


def update_job_offer(dto: UpdateJobOfferDto, id: int):  # noqa: E501
    """Updates a job offer by its id.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes
    :param id:
    :type id: int

    :rtype: None
    """
    return 'do some magic!'
