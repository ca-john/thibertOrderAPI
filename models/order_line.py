# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class OrderLine(object):
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
        'quantity': 'int'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'quantity': 'quantity'
    }

    def __init__(self, thibert_part_number=None, quantity=None):  # noqa: E501
        """OrderLine - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._quantity = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if quantity is not None:
            self.quantity = quantity

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this OrderLine.  # noqa: E501

        Part number in the Thibert database.  # noqa: E501

        :return: The thibert_part_number of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this OrderLine.

        Part number in the Thibert database.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this OrderLine.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def quantity(self):
        """Gets the quantity of this OrderLine.  # noqa: E501

        Quantity to ship.  # noqa: E501

        :return: The quantity of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderLine.

        Quantity to ship.  # noqa: E501

        :param quantity: The quantity of this OrderLine.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(OrderLine, dict):
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
        if not isinstance(other, OrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
