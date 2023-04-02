# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class Inventory(object):
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
        'quantity': 'int',
        'site_code': 'str',
        'is_primary_site': 'bool'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'quantity': 'quantity',
        'site_code': 'siteCode',
        'is_primary_site': 'isPrimarySite'
    }

    def __init__(self, thibert_part_number=None, quantity=None, site_code=None, is_primary_site=None):  # noqa: E501
        """Inventory - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._quantity = None
        self._site_code = None
        self._is_primary_site = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if quantity is not None:
            self.quantity = quantity
        if site_code is not None:
            self.site_code = site_code
        if is_primary_site is not None:
            self.is_primary_site = is_primary_site

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this Inventory.  # noqa: E501

        Part number of the item associated with this inventory.  # noqa: E501

        :return: The thibert_part_number of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this Inventory.

        Part number of the item associated with this inventory.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this Inventory.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def quantity(self):
        """Gets the quantity of this Inventory.  # noqa: E501

        The quantity in the location of this inventory.  # noqa: E501

        :return: The quantity of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Inventory.

        The quantity in the location of this inventory.  # noqa: E501

        :param quantity: The quantity of this Inventory.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def site_code(self):
        """Gets the site_code of this Inventory.  # noqa: E501

        The site code of this inventory.  # noqa: E501

        :return: The site_code of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        """Sets the site_code of this Inventory.

        The site code of this inventory.  # noqa: E501

        :param site_code: The site_code of this Inventory.  # noqa: E501
        :type: str
        """

        self._site_code = site_code

    @property
    def is_primary_site(self):
        """Gets the is_primary_site of this Inventory.  # noqa: E501

        Indicates if this is the main site for this account  # noqa: E501

        :return: The is_primary_site of this Inventory.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_site

    @is_primary_site.setter
    def is_primary_site(self, is_primary_site):
        """Sets the is_primary_site of this Inventory.

        Indicates if this is the main site for this account  # noqa: E501

        :param is_primary_site: The is_primary_site of this Inventory.  # noqa: E501
        :type: bool
        """

        self._is_primary_site = is_primary_site

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
        if issubclass(Inventory, dict):
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
        if not isinstance(other, Inventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
