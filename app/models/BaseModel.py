import pprint
import typing

T = typing.TypeVar('T')


class BaseModel(object):
    _data = {}

    def to_dict(self) -> dict:
        """Returns the model as a dict

        :return: The dict of this UpdateJobOfferDto.  # noqa: E501
        :rtype: dict
        """
        return dict(self._data)

    def to_str(self):
        """Returns the string representation of the model

        :rtype: str
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
