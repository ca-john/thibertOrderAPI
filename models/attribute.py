# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class Attribute(object):
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
        'attribute_id': 'str',
        'attribute_names': 'list[LocalizedString]',
        'attribute_values': 'list[LocalizedString]'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'attribute_id': 'attributeID',
        'attribute_names': 'attributeNames',
        'attribute_values': 'attributeValues'
    }

    def __init__(self, thibert_part_number=None, attribute_id=None, attribute_names=None, attribute_values=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._attribute_id = None
        self._attribute_names = None
        self._attribute_values = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if attribute_id is not None:
            self.attribute_id = attribute_id
        if attribute_names is not None:
            self.attribute_names = attribute_names
        if attribute_values is not None:
            self.attribute_values = attribute_values

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this Attribute.  # noqa: E501

        Part number of the item associated with this attribute.  # noqa: E501

        :return: The thibert_part_number of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this Attribute.

        Part number of the item associated with this attribute.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this Attribute.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def attribute_id(self):
        """Gets the attribute_id of this Attribute.  # noqa: E501

        ID of this attribute.  # noqa: E501

        :return: The attribute_id of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this Attribute.

        ID of this attribute.  # noqa: E501

        :param attribute_id: The attribute_id of this Attribute.  # noqa: E501
        :type: str
        """

        self._attribute_id = attribute_id

    @property
    def attribute_names(self):
        """Gets the attribute_names of this Attribute.  # noqa: E501

        Name of this attribute.  # noqa: E501

        :return: The attribute_names of this Attribute.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._attribute_names

    @attribute_names.setter
    def attribute_names(self, attribute_names):
        """Sets the attribute_names of this Attribute.

        Name of this attribute.  # noqa: E501

        :param attribute_names: The attribute_names of this Attribute.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._attribute_names = attribute_names

    @property
    def attribute_values(self):
        """Gets the attribute_values of this Attribute.  # noqa: E501

        Value of this attribute.  # noqa: E501

        :return: The attribute_values of this Attribute.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._attribute_values

    @attribute_values.setter
    def attribute_values(self, attribute_values):
        """Sets the attribute_values of this Attribute.

        Value of this attribute.  # noqa: E501

        :param attribute_values: The attribute_values of this Attribute.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._attribute_values = attribute_values

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
