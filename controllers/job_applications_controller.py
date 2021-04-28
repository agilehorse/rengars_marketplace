from datetime import datetime

import connexion

from models.CreateJobApplicationDto import CreateJobApplicationDto
from models.JobApplicationState import JobApplicationState  # noqa: E501
from models.RestException import RestException
from services.JobApplicationService import JobApplicationService
from utils.utils import get_error_dto


def change_job_application_state(id: int):  # noqa: E501
    """Changes a state of a job application by its id.

     # noqa: E501

    :param id:
    :type id: int

    :rtype: None
    """
    search_id_query = {"_id": id}
    try:
        new_state = connexion.request.json.get('state')
        update_object = {"state": new_state}
        if JobApplicationState.is_readonly(new_state):
            update_object['dateClosed'] = datetime.now()

        JobApplicationService.update_job_application(search_id_query, update_object)
        return None, 200
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")


def create_job_application():  # noqa: E501
    """Creates a job application.

     # noqa: E501

    :rtype: GetJobApplicationDto
    """
    try:
        dto = CreateJobApplicationDto.from_dict(connexion.request.json)
        JobApplicationService.create_job_application(dto)
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
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
    search_id_query = {"_id": id}
    try:
        job_application = JobApplicationService.find_job_application(search_id_query)
        return job_application, 200
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")


def get_job_applications():  # noqa: E501
    """Gets all Job applications.

     # noqa: E501


    :rtype: List[JobApplication]
    """
    try:
        job_applications = JobApplicationService.find_job_applications()
        return job_applications, 200
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
    new_note = connexion.request.json.get('note')
    update_object = {"note": new_note}
    try:
        JobApplicationService.update_job_application(search_id_query, update_object)
        return None, 200
    except RestException as re:
        print(re)
        return get_error_dto(re.error_type, re.status_code, re.info)
    except Exception as e:
        print(e)
        return get_error_dto("errors.job_applications.unknown")
