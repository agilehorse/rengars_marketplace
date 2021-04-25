# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models.BaseModel import BaseModel
from models.CreateJobApplicationDto import CreateJobApplicationDto  # noqa: E501
from models.JobApplicationState import JobApplicationState  # noqa: F401,E501
from models.User import User  # noqa: F401,E501

id = '_id'
applicant = 'applicant'
note = 'note'
jobOfferId = 'jobOfferId'
state = 'state'
dateCreated = 'dateCreated'
dateClosed = 'dateClosed'


class JobApplication(BaseModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, new_id: int = None, new_applicant: User = None, new_note: str = None,
                 new_job_offer_id: int = None, new_state: JobApplicationState = None,
                 new_date_created: datetime = None, new_date_closed: datetime = None):  # noqa: E501
        """JobApplication - a model defined in Swagger

        :param new_id: The id of this JobApplication.  # noqa: E501
        :type new_id: int
        :param new_applicant: The applicant of this JobApplication.  # noqa: E501
        :type new_applicant: User
        :param new_note: The note of this JobApplication.  # noqa: E501
        :type new_note: str
        :param new_job_offer_id: The job_offer_id of this JobApplication.  # noqa: E501
        :type new_job_offer_id: int
        :param new_state: The state of this JobApplication.  # noqa: E501
        :type new_state: JobApplicationState
        :param new_date_created: The date_created of this JobApplication.  # noqa: E501
        :type new_date_created: datetime
        :param new_date_closed: The date_closed of this JobApplication.  # noqa: E501
        :type new_date_closed: datetime
        """
        self._data = {
            id: new_id,
            applicant: new_applicant,
            note: new_note,
            state: new_state,
            jobOfferId: new_job_offer_id,
            dateCreated: new_date_created,
            dateClosed: new_date_closed
        }

    @classmethod
    def from_dict(cls, dikt) -> 'JobApplication':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobApplication of this JobApplication.  # noqa: E501
        :rtype: JobApplication
        """
        instance = cls()
        instance.id = dikt.get('id')
        instance.applicant = User.from_dict(dikt.get(applicant))
        instance.note = dikt.get(note)
        instance.state = dikt.get(state)
        instance.job_offer_id = dikt.get(jobOfferId)
        instance.date_created = dikt.get(dateCreated)
        instance.date_closed = dikt.get(dateClosed)
        return instance

    def to_dict(self) -> dict:
        """Returns the model as a dict

        :return: The dict of this JobApplication.  # noqa: E501
        :rtype: dict
        """
        dikt = dict(self._data)
        dikt[applicant] = User.to_dict(self.applicant)
        return dikt

    @classmethod
    def from_dto(cls, dto: CreateJobApplicationDto) -> 'JobApplication':
        """Returns instance from dto

        :param dto: A dto.
        :type: CreateJobApplicationDto
        :return: The instance of this JobApplication.  # noqa: E501
        :rtype: JobApplication
        """
        instance = cls()
        instance.note = dto.note
        instance.job_offer_id = dto.job_offer_id
        return instance

    @property
    def id(self) -> int:
        """Gets the id of this JobApplication.


        :return: The id of this JobApplication.
        :rtype: int
        """
        return self._data[id]

    @id.setter
    def id(self, new_id: int):
        """Sets the id of this JobApplication.


        :param new_id: The id of this JobApplication.
        :type new_id: int
        """
        if new_id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._data[id] = new_id

    @property
    def applicant(self) -> User:
        """Gets the applicant of this JobApplication.


        :return: The applicant of this JobApplication.
        :rtype: User
        """
        return self._data[applicant]

    @applicant.setter
    def applicant(self, new_applicant: User):
        """Sets the applicant of this JobApplication.


        :param new_applicant: The applicant of this JobApplication.
        :type new_applicant: User
        """
        if new_applicant is None:
            raise ValueError("Invalid value for `applicant`, must not be `None`")  # noqa: E501

        self._data[applicant] = new_applicant

    @property
    def note(self) -> str:
        """Gets the note of this JobApplication.


        :return: The note of this JobApplication.
        :rtype: str
        """
        return self._data[note]

    @note.setter
    def note(self, new_note: str):
        """Sets the note of this JobApplication.


        :param new_note: The note of this JobApplication.
        :type new_note: str
        """
        if new_note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._data[note] = new_note

    @property
    def job_offer_id(self) -> int:
        """Gets the job_offer_id of this JobApplication.


        :return: The job_offer_id of this JobApplication.
        :rtype: int
        """
        return self._data[jobOfferId]

    @job_offer_id.setter
    def job_offer_id(self, new_job_offer_id: int):
        """Sets the job_offer_id of this JobApplication.


        :param new_job_offer_id: The job_offer_id of this JobApplication.
        :type new_job_offer_id: int
        """
        if new_job_offer_id is None:
            raise ValueError("Invalid value for `job_offer_id`, must not be `None`")  # noqa: E501

        self._data[jobOfferId] = new_job_offer_id

    @property
    def state(self) -> JobApplicationState:
        """Gets the state of this JobApplication.


        :return: The state of this JobApplication.
        :rtype: JobApplicationState
        """
        return self._data[state]

    @state.setter
    def state(self, new_state: JobApplicationState):
        """Sets the state of this JobApplication.


        :param new_state: The state of this JobApplication.
        :type new_state: JobApplicationState
        """

        self._data[state] = new_state

    @property
    def date_created(self) -> datetime:
        """Gets the date_created of this JobApplication.


        :return: The date_created of this JobApplication.
        :rtype: datetime
        """
        return self._data[dateCreated]

    @date_created.setter
    def date_created(self, new_date_created: datetime):
        """Sets the date_created of this JobApplication.


        :param new_date_created: The date_created of this JobApplication.
        :type new_date_created: datetime
        """

        self._data[dateCreated] = new_date_created

    @property
    def date_closed(self) -> datetime:
        """Gets the date_closed of this JobApplication.


        :return: The date_closed of this JobApplication.
        :rtype: datetime
        """
        return self._data[dateClosed]

    @date_closed.setter
    def date_closed(self, new_date_closed: datetime):
        """Sets the date_closed of this JobApplication.


        :param new_date_closed: The date_closed of this JobApplication.
        :type new_date_closed: datetime
        """

        self._data[dateClosed] = new_date_closed
