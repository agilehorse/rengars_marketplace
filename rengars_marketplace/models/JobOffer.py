# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from rengars_marketplace import util
from rengars_marketplace.models.BaseModel import BaseModel
from rengars_marketplace.models.JobApplication import JobApplication  # noqa: F401,E501
from rengars_marketplace.models.JobOfferState import JobOfferState  # noqa: F401,E501
from rengars_marketplace.models.User import User  # noqa: F401,E501


class JobOffer(BaseModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int = None, poster: User = None, company_name: str = None, position_name: str = None,
                 description: str = None, state: JobOfferState = None, date_created: datetime = None,
                 date_ended: datetime = None, job_applications: List[JobApplication] = None):  # noqa: E501
        """JobOffer - a model defined in Swagger

        :param id: The id of this JobOffer.  # noqa: E501
        :type id: int
        :param poster: The poster of this JobOffer.  # noqa: E501
        :type poster: User
        :param company_name: The company_name of this JobOffer.  # noqa: E501
        :type company_name: str
        :param position_name: The position_name of this JobOffer.  # noqa: E501
        :type position_name: str
        :param description: The description of this JobOffer.  # noqa: E501
        :type description: str
        :param state: The state of this JobOffer.  # noqa: E501
        :type state: JobOfferState
        :param date_created: The date_created of this JobOffer.  # noqa: E501
        :type date_created: datetime
        :param date_ended: The date_ended of this JobOffer.  # noqa: E501
        :type date_ended: datetime
        :param job_applications: The job_applications of this JobOffer.  # noqa: E501
        :type job_applications: List[JobApplication]
        """
        self.swagger_types = {
            'id': int,
            'poster': User,
            'company_name': str,
            'position_name': str,
            'description': str,
            'state': JobOfferState,
            'date_created': datetime,
            'date_ended': datetime,
            'job_applications': List[JobApplication]
        }

        self.attribute_map = {
            'id': 'id',
            'poster': 'poster',
            'company_name': 'companyName',
            'position_name': 'positionName',
            'description': 'description',
            'state': 'state',
            'date_created': 'dateCreated',
            'date_ended': 'dateEnded',
            'job_applications': 'jobApplications'
        }
        self._id = id
        self._poster = poster
        self._company_name = company_name
        self._position_name = position_name
        self._description = description
        self._state = state
        self._date_created = date_created
        self._date_ended = date_ended
        self._job_applications = job_applications

    @classmethod
    def from_dict(cls, dikt) -> 'JobOffer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobOffer of this JobOffer.  # noqa: E501
        :rtype: JobOffer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this JobOffer.


        :return: The id of this JobOffer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this JobOffer.


        :param id: The id of this JobOffer.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def poster(self) -> User:
        """Gets the poster of this JobOffer.


        :return: The poster of this JobOffer.
        :rtype: User
        """
        return self._poster

    @poster.setter
    def poster(self, poster: User):
        """Sets the poster of this JobOffer.


        :param poster: The poster of this JobOffer.
        :type poster: User
        """
        if poster is None:
            raise ValueError("Invalid value for `poster`, must not be `None`")  # noqa: E501

        self._poster = poster

    @property
    def company_name(self) -> str:
        """Gets the company_name of this JobOffer.


        :return: The company_name of this JobOffer.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str):
        """Sets the company_name of this JobOffer.


        :param company_name: The company_name of this JobOffer.
        :type company_name: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def position_name(self) -> str:
        """Gets the position_name of this JobOffer.


        :return: The position_name of this JobOffer.
        :rtype: str
        """
        return self._position_name

    @position_name.setter
    def position_name(self, position_name: str):
        """Sets the position_name of this JobOffer.


        :param position_name: The position_name of this JobOffer.
        :type position_name: str
        """
        if position_name is None:
            raise ValueError("Invalid value for `position_name`, must not be `None`")  # noqa: E501

        self._position_name = position_name

    @property
    def description(self) -> str:
        """Gets the description of this JobOffer.


        :return: The description of this JobOffer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this JobOffer.


        :param description: The description of this JobOffer.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def state(self) -> JobOfferState:
        """Gets the state of this JobOffer.


        :return: The state of this JobOffer.
        :rtype: JobOfferState
        """
        return self._state

    @state.setter
    def state(self, state: JobOfferState):
        """Sets the state of this JobOffer.


        :param state: The state of this JobOffer.
        :type state: JobOfferState
        """

        self._state = state

    @property
    def date_created(self) -> datetime:
        """Gets the date_created of this JobOffer.


        :return: The date_created of this JobOffer.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime):
        """Sets the date_created of this JobOffer.


        :param date_created: The date_created of this JobOffer.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_ended(self) -> datetime:
        """Gets the date_ended of this JobOffer.


        :return: The date_ended of this JobOffer.
        :rtype: datetime
        """
        return self._date_ended

    @date_ended.setter
    def date_ended(self, date_ended: datetime):
        """Sets the date_ended of this JobOffer.


        :param date_ended: The date_ended of this JobOffer.
        :type date_ended: datetime
        """

        self._date_ended = date_ended

    @property
    def job_applications(self) -> List[JobApplication]:
        """Gets the job_applications of this JobOffer.


        :return: The job_applications of this JobOffer.
        :rtype: List[JobApplication]
        """
        return self._job_applications

    @job_applications.setter
    def job_applications(self, job_applications: List[JobApplication]):
        """Sets the job_applications of this JobOffer.


        :param job_applications: The job_applications of this JobOffer.
        :type job_applications: List[JobApplication]
        """

        self._job_applications = job_applications
