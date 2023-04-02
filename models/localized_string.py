# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class LocalizedString(object):
    """

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'language_code': 'str',
        'localized_value': 'str'
    }

    attribute_map = {
        'language_code': 'languageCode',
        'localized_value': 'localizedValue'
    }

    def __init__(self, language_code=None, localized_value=None):  # noqa: E501
        """LocalizedString - a model defined in Swagger"""  # noqa: E501
        self._language_code = None
        self._localized_value = None
        self.discriminator = None
        if language_code is not None:
            self.language_code = language_code
        if localized_value is not None:
            self.localized_value = localized_value

    @property
    def language_code(self):
        """Gets the language_code of this LocalizedString.  # noqa: E501


        :return: The language_code of this LocalizedString.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this LocalizedString.


        :param language_code: The language_code of this LocalizedString.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def localized_value(self):
        """Gets the localized_value of this LocalizedString.  # noqa: E501


        :return: The localized_value of this LocalizedString.  # noqa: E501
        :rtype: str
        """
        return self._localized_value

    @localized_value.setter
    def localized_value(self, localized_value):
        """Sets the localized_value of this LocalizedString.


        :param localized_value: The localized_value of this LocalizedString.  # noqa: E501
        :type: str
        """

        self._localized_value = localized_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LocalizedString, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LocalizedString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other