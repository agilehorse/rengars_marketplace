# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from rengars_marketplace import util
from rengars_marketplace.models.Model import Model


class ErrorDto(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str = None, message: str = None):  # noqa: E501
        """ErrorDto - a model defined in Swagger

        :param type: The type of this ErrorDto.  # noqa: E501
        :type type: str
        :param message: The message of this ErrorDto.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'type': str,
            'message': str
        }

        self.attribute_map = {
            'type': 'type',
            'message': 'message'
        }
        self._type = type
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorDto of this ErrorDto.  # noqa: E501
        :rtype: ErrorDto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ErrorDto.

        Unique id of the error  # noqa: E501

        :return: The type of this ErrorDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ErrorDto.

        Unique id of the error  # noqa: E501

        :param type: The type of this ErrorDto.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def message(self) -> str:
        """Gets the message of this ErrorDto.

        Error message  # noqa: E501

        :return: The message of this ErrorDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ErrorDto.

        Error message  # noqa: E501

        :param message: The message of this ErrorDto.
        :type message: str
        """

        self._message = message
