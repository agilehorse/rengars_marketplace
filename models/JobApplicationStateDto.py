# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models.BaseModel import BaseModel
from models.JobApplicationState import JobApplicationState  # noqa: F401,E501

state = 'state'


class JobApplicationStateDto(BaseModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, new_state: JobApplicationState = None):  # noqa: E501
        """JobApplicationStateDto - a model defined in Swagger

        :param state: The state of this JobApplicationStateDto.  # noqa: E501
        :type state: JobApplicationState
        """
        self._data = {
            state: new_state
        }

    @classmethod
    def from_dict(cls, dikt) -> 'JobApplicationStateDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobApplicationStateDto of this JobApplicationStateDto.  # noqa: E501
        :rtype: JobApplicationStateDto
        """
        instance = cls()
        instance.state = dikt[state]
        return instance

    @property
    def state(self) -> JobApplicationState:
        """Gets the state of this JobApplicationStateDto.


        :return: The state of this JobApplicationStateDto.
        :rtype: JobApplicationState
        """
        return self._data[state]

    @state.setter
    def state(self, new_state: JobApplicationState):
        """Sets the state of this JobApplicationStateDto.


        :param new_state: The state of this JobApplicationStateDto.
        :type new_state: JobApplicationState
        """

        self._data[state] = new_state