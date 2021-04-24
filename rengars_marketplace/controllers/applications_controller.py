from rengars_marketplace.models.CreateJobApplicationDto import CreateJobApplicationDto  # noqa: E501
from rengars_marketplace.models.JobApplication import JobApplication  # noqa: E501
from rengars_marketplace.models.JobApplicationStateDto import JobApplicationStateDto  # noqa: E501
from rengars_marketplace.models.UpdateJobApplicationDto import UpdateJobApplicationDto  # noqa: E501


def change_job_application_state(dto: JobApplicationStateDto, id: int):  # noqa: E501
    """Changes a state of a job application by its id.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes
    :param id:
    :type id: int

    :rtype: None
    """

    return 'do some magic!'


def create_job_application(dto: CreateJobApplicationDto):  # noqa: E501
    """Creates a job application.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes

    :rtype: JobApplication
    """
    return 'do some magic!'


def get_job_application(id: int):  # noqa: E501
    """Gets a job application by its id.

     # noqa: E501

    :param id:
    :type id: int

    :rtype: JobApplication
    """
    return 'do some magic!'


def get_job_applications():  # noqa: E501
    """Gets all Job applications.

     # noqa: E501


    :rtype: List[JobApplication]
    """
    return 'do some magic!'


def update_job_application(dto: UpdateJobApplicationDto, id: int):  # noqa: E501
    """Updates an application by its id.

     # noqa: E501

    :param dto:
    :type dto: dict | bytes
    :param id:
    :type id: int

    :rtype: None
    """
    return 'do some magic!'
