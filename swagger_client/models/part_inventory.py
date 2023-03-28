# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class PartInventory(object):
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
        'inventories': 'list[Inventory]'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'inventories': 'inventories'
    }

    def __init__(self, thibert_part_number=None, inventories=None):  # noqa: E501
        """PartInventory - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._inventories = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if inventories is not None:
            self.inventories = inventories

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this PartInventory.  # noqa: E501

        Thibert part number associated with this item.  # noqa: E501

        :return: The thibert_part_number of this PartInventory.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this PartInventory.

        Thibert part number associated with this item.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this PartInventory.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def inventories(self):
        """Gets the inventories of this PartInventory.  # noqa: E501

        List of all inventories associated with this item.  # noqa: E501

        :return: The inventories of this PartInventory.  # noqa: E501
        :rtype: list[Inventory]
        """
        return self._inventories

    @inventories.setter
    def inventories(self, inventories):
        """Sets the inventories of this PartInventory.

        List of all inventories associated with this item.  # noqa: E501

        :param inventories: The inventories of this PartInventory.  # noqa: E501
        :type: list[Inventory]
        """

        self._inventories = inventories

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
        if issubclass(PartInventory, dict):
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
        if not isinstance(other, PartInventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
