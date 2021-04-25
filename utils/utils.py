import connexion
from connexion.lifecycle import ConnexionResponse
from pymongo import ReturnDocument

from App import db
from models.JobApplicationState import JobApplicationState
from models.JobOfferState import JobOfferState


def get_next_sequence(name):
    return db.counters.find_one_and_update(
        {'_id': name},
        {'$inc': {'seq': 1}},
        projection={'seq': True, '_id': False},
        upsert=True,
        return_document=ReturnDocument.AFTER
    ).get('seq')


def validate_job_application(job_application: dict):
    if job_application is None:
        return get_error_dto("errors.job_applications.not_found", 404)
    state = job_application['state']
    if JobApplicationState.is_readonly(state):
        return get_error_dto("errors.job_applications.read_only", 409, state)
    return None


def validate_job_offer(job_offer: dict, new_state=None):
    if job_offer is None:
        return get_error_dto("errors.job_offers.not_found", 404)
    state = job_offer['state']
    if JobOfferState.is_readonly(state):
        return get_error_dto("errors.job_offers.read_only", 409, state)
    if new_state == JobOfferState.WITHDRAWN:
        accepted = list(db.job_applications.find({"jobOfferId": id, "state": JobApplicationState.ACCEPTED}))
        if len(accepted) > 0:
            return get_error_dto("errors.job_offers.withdrawing_accepted")
    return None


def remap_id(json: dict) -> dict:
    json['id'] = json.pop('_id')
    return json


static_errors = {
    "errors.job_applications.not_found": connexion.problem(404, 'Not found',
                                                           "Job application with this id does not exist!",
                                                           "errors.job_applications.not_found"),
    "errors.job_applications.unknown": connexion.problem(400, 'Bad request',
                                                         "An unknown error occurred, please try again later.",
                                                         "errors.job_applications.unknown"),
    "errors.job_offers.not_found": connexion.problem(404, 'Not found',
                                                     "Job offer with this id does not exist!",
                                                     "errors.job_offers.not_found"),
    "errors.job_offers.unknown": connexion.problem(400, 'Bad request',
                                                   "An unknown error occurred, please try again later.",
                                                   "errors.job_offers.unknown"),
    "errors.job_offers.withdrawing_accepted": connexion.problem(409, 'Bad request',
                                                                "Cannot withdraw a job offer for which there are some accepted applications!",
                                                                "errors.job_offers.withdrawing_accepted"),
}
non_static_errors = {
    "errors.job_applications.read_only": "Cannot change the application which has a final state: {}!",
    "errors.job_offers.read_only": "Cannot change the job offer which has a final state: {}!",
}
http_status_title = {
    400: 'Bad request',
    404: 'Not found',
    409: 'Conflict'
}


def get_error_dto(error_type: str, http_status_code=400, parameter=None) -> ConnexionResponse:
    if parameter is None:
        return static_errors[error_type]

    return connexion.problem(http_status_code, http_status_title[http_status_code],
                             non_static_errors[error_type].format(parameter), error_type)
