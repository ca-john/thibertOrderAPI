# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class Taxline(object):
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
        'tax_id': 'str',
        'description': 'str',
        'percentage': 'float',
        'amount': 'float'
    }

    attribute_map = {
        'tax_id': 'taxId',
        'description': 'description',
        'percentage': 'percentage',
        'amount': 'amount'
    }

    def __init__(self, tax_id=None, description=None, percentage=None, amount=None):  # noqa: E501
        """Taxline - a model defined in Swagger"""  # noqa: E501
        self._tax_id = None
        self._description = None
        self._percentage = None
        self._amount = None
        self.discriminator = None
        if tax_id is not None:
            self.tax_id = tax_id
        if description is not None:
            self.description = description
        if percentage is not None:
            self.percentage = percentage
        if amount is not None:
            self.amount = amount

    @property
    def tax_id(self):
        """Gets the tax_id of this Taxline.  # noqa: E501


        :return: The tax_id of this Taxline.  # noqa: E501
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """Sets the tax_id of this Taxline.


        :param tax_id: The tax_id of this Taxline.  # noqa: E501
        :type: str
        """

        self._tax_id = tax_id

    @property
    def description(self):
        """Gets the description of this Taxline.  # noqa: E501


        :return: The description of this Taxline.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Taxline.


        :param description: The description of this Taxline.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def percentage(self):
        """Gets the percentage of this Taxline.  # noqa: E501


        :return: The percentage of this Taxline.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Taxline.


        :param percentage: The percentage of this Taxline.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def amount(self):
        """Gets the amount of this Taxline.  # noqa: E501


        :return: The amount of this Taxline.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Taxline.


        :param amount: The amount of this Taxline.  # noqa: E501
        :type: float
        """

        self._amount = amount

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
        if issubclass(Taxline, dict):
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
        if not isinstance(other, Taxline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
