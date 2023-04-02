# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class PartIsVehicleSpecific(object):
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
        'is_vehicle_specific': 'bool'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'is_vehicle_specific': 'isVehicleSpecific'
    }

    def __init__(self, thibert_part_number=None, is_vehicle_specific=None):  # noqa: E501
        """PartIsVehicleSpecific - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._is_vehicle_specific = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if is_vehicle_specific is not None:
            self.is_vehicle_specific = is_vehicle_specific

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this PartIsVehicleSpecific.  # noqa: E501

        ThibertPartNumber validated  # noqa: E501

        :return: The thibert_part_number of this PartIsVehicleSpecific.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this PartIsVehicleSpecific.

        ThibertPartNumber validated  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this PartIsVehicleSpecific.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def is_vehicle_specific(self):
        """Gets the is_vehicle_specific of this PartIsVehicleSpecific.  # noqa: E501

        Indicates if there is a specific fitment for this part  # noqa: E501

        :return: The is_vehicle_specific of this PartIsVehicleSpecific.  # noqa: E501
        :rtype: bool
        """
        return self._is_vehicle_specific

    @is_vehicle_specific.setter
    def is_vehicle_specific(self, is_vehicle_specific):
        """Sets the is_vehicle_specific of this PartIsVehicleSpecific.

        Indicates if there is a specific fitment for this part  # noqa: E501

        :param is_vehicle_specific: The is_vehicle_specific of this PartIsVehicleSpecific.  # noqa: E501
        :type: bool
        """

        self._is_vehicle_specific = is_vehicle_specific

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
        if issubclass(PartIsVehicleSpecific, dict):
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
        if not isinstance(other, PartIsVehicleSpecific):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
