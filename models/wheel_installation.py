# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class WheelInstallation(object):
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
        'thibert_part_number': 'str',
        'wheel_installation_kits': 'list[WheelInstallationKit]',
        'wheel_installation_parts': 'list[WheelInstallationPart]'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'wheel_installation_kits': 'wheelInstallationKits',
        'wheel_installation_parts': 'wheelInstallationParts'
    }

    def __init__(self, thibert_part_number=None, wheel_installation_kits=None, wheel_installation_parts=None):  # noqa: E501
        """WheelInstallation - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._wheel_installation_kits = None
        self._wheel_installation_parts = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if wheel_installation_kits is not None:
            self.wheel_installation_kits = wheel_installation_kits
        if wheel_installation_parts is not None:
            self.wheel_installation_parts = wheel_installation_parts

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this WheelInstallation.  # noqa: E501

        Thibert part number  # noqa: E501

        :return: The thibert_part_number of this WheelInstallation.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this WheelInstallation.

        Thibert part number  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this WheelInstallation.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def wheel_installation_kits(self):
        """Gets the wheel_installation_kits of this WheelInstallation.  # noqa: E501


        :return: The wheel_installation_kits of this WheelInstallation.  # noqa: E501
        :rtype: list[WheelInstallationKit]
        """
        return self._wheel_installation_kits

    @wheel_installation_kits.setter
    def wheel_installation_kits(self, wheel_installation_kits):
        """Sets the wheel_installation_kits of this WheelInstallation.


        :param wheel_installation_kits: The wheel_installation_kits of this WheelInstallation.  # noqa: E501
        :type: list[WheelInstallationKit]
        """

        self._wheel_installation_kits = wheel_installation_kits

    @property
    def wheel_installation_parts(self):
        """Gets the wheel_installation_parts of this WheelInstallation.  # noqa: E501


        :return: The wheel_installation_parts of this WheelInstallation.  # noqa: E501
        :rtype: list[WheelInstallationPart]
        """
        return self._wheel_installation_parts

    @wheel_installation_parts.setter
    def wheel_installation_parts(self, wheel_installation_parts):
        """Sets the wheel_installation_parts of this WheelInstallation.


        :param wheel_installation_parts: The wheel_installation_parts of this WheelInstallation.  # noqa: E501
        :type: list[WheelInstallationPart]
        """

        self._wheel_installation_parts = wheel_installation_parts

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
        if issubclass(WheelInstallation, dict):
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
        if not isinstance(other, WheelInstallation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
