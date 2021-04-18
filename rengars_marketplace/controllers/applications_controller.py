import connexion
import six

from rengars_marketplace.models.CreateJobApplicationDto import CreateJobApplicationDto  # noqa: E501
from rengars_marketplace.models.ErrorDto import ErrorDto  # noqa: E501
from rengars_marketplace.models.JobApplication import JobApplication  # noqa: E501
from rengars_marketplace.models.JobApplicationStateDto import JobApplicationStateDto  # noqa: E501
from rengars_marketplace.models.UpdateJobApplicationDto import UpdateJobApplicationDto  # noqa: E501
from rengars_marketplace import util


def marketplace_job_applications_get():  # noqa: E501
    """Gets all Job applications.

     # noqa: E501


    :rtype: List[JobApplication]
    """
    return 'do some magic!'


def marketplace_job_applications_id_change_state_put(body, id):  # noqa: E501
    """Changes a state of a job application by its id.

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = JobApplicationStateDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def marketplace_job_applications_id_get(id):  # noqa: E501
    """Gets a job application by its id.

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: JobApplication
    """
    return 'do some magic!'


def marketplace_job_applications_id_put(body, id):  # noqa: E501
    """Updates an application by its id.

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateJobApplicationDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def marketplace_job_applications_post(body):  # noqa: E501
    """Creates a job application.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: JobApplication
    """
    if connexion.request.is_json:
        body = CreateJobApplicationDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
