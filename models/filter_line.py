# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class FilterLine(object):
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
        'filter_name': 'str',
        'filter_values': 'list[str]'
    }

    attribute_map = {
        'filter_name': 'filterName',
        'filter_values': 'filterValues'
    }

    def __init__(self, filter_name=None, filter_values=None):  # noqa: E501
        """FilterLine - a model defined in Swagger"""  # noqa: E501
        self._filter_name = None
        self._filter_values = None
        self.discriminator = None
        if filter_name is not None:
            self.filter_name = filter_name
        if filter_values is not None:
            self.filter_values = filter_values

    @property
    def filter_name(self):
        """Gets the filter_name of this FilterLine.  # noqa: E501

        Available filters name: ThibertPartNumber, VendorPartNumber, WheelPartTypeID, Brand, Diameter, Width, BoltPattern, CenterBore, Offset, CategoryId, LastModificationDate  # noqa: E501

        :return: The filter_name of this FilterLine.  # noqa: E501
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """Sets the filter_name of this FilterLine.

        Available filters name: ThibertPartNumber, VendorPartNumber, WheelPartTypeID, Brand, Diameter, Width, BoltPattern, CenterBore, Offset, CategoryId, LastModificationDate  # noqa: E501

        :param filter_name: The filter_name of this FilterLine.  # noqa: E501
        :type: str
        """

        self._filter_name = filter_name

    @property
    def filter_values(self):
        """Gets the filter_values of this FilterLine.  # noqa: E501

        Example of possible filter values (not exhaustive)  <br />  ThibertPartNumber: 081001, 00021, 00030, 00076  <br />  VendorPartNumber: 32571885114342731MM1, 49581, 8LTC49K  <br />  WheelPartTypeID: 00020, 00021, 00030, 00076  <br />  Brand: RTX, Ceco, Black Rhino ...  <br />  Diameter: 17, 18, 19 ...  <br />  Width: 6, 8, 9.5 ...  <br />  BoltPattern: 5x114.3, 6x132, 8x165.1 ...  <br />  CenterBore: 60.1, 108, 130.8  <br />  Offset: -13, 27, 52.5  <br />  CategoryId: 0360, 026 ...  <br />  LastModificationDate: 12/31/2023  # noqa: E501

        :return: The filter_values of this FilterLine.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_values

    @filter_values.setter
    def filter_values(self, filter_values):
        """Sets the filter_values of this FilterLine.

        Example of possible filter values (not exhaustive)  <br />  ThibertPartNumber: 081001, 00021, 00030, 00076  <br />  VendorPartNumber: 32571885114342731MM1, 49581, 8LTC49K  <br />  WheelPartTypeID: 00020, 00021, 00030, 00076  <br />  Brand: RTX, Ceco, Black Rhino ...  <br />  Diameter: 17, 18, 19 ...  <br />  Width: 6, 8, 9.5 ...  <br />  BoltPattern: 5x114.3, 6x132, 8x165.1 ...  <br />  CenterBore: 60.1, 108, 130.8  <br />  Offset: -13, 27, 52.5  <br />  CategoryId: 0360, 026 ...  <br />  LastModificationDate: 12/31/2023  # noqa: E501

        :param filter_values: The filter_values of this FilterLine.  # noqa: E501
        :type: list[str]
        """

        self._filter_values = filter_values

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
        if issubclass(FilterLine, dict):
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
        if not isinstance(other, FilterLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
