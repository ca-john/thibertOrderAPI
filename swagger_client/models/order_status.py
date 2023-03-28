# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class OrderStatus(object):
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
        'thibert_order_number': 'str',
        'order_reference_number': 'str',
        'status': 'str'
    }

    attribute_map = {
        'thibert_order_number': 'thibertOrderNumber',
        'order_reference_number': 'orderReferenceNumber',
        'status': 'status'
    }

    def __init__(self, thibert_order_number=None, order_reference_number=None, status=None):  # noqa: E501
        """OrderStatus - a model defined in Swagger"""  # noqa: E501
        self._thibert_order_number = None
        self._order_reference_number = None
        self._status = None
        self.discriminator = None
        if thibert_order_number is not None:
            self.thibert_order_number = thibert_order_number
        if order_reference_number is not None:
            self.order_reference_number = order_reference_number
        if status is not None:
            self.status = status

    @property
    def thibert_order_number(self):
        """Gets the thibert_order_number of this OrderStatus.  # noqa: E501

        Indicates the Thibert Order Number  # noqa: E501

        :return: The thibert_order_number of this OrderStatus.  # noqa: E501
        :rtype: str
        """
        return self._thibert_order_number

    @thibert_order_number.setter
    def thibert_order_number(self, thibert_order_number):
        """Sets the thibert_order_number of this OrderStatus.

        Indicates the Thibert Order Number  # noqa: E501

        :param thibert_order_number: The thibert_order_number of this OrderStatus.  # noqa: E501
        :type: str
        """

        self._thibert_order_number = thibert_order_number

    @property
    def order_reference_number(self):
        """Gets the order_reference_number of this OrderStatus.  # noqa: E501

        Client order number reference.  # noqa: E501

        :return: The order_reference_number of this OrderStatus.  # noqa: E501
        :rtype: str
        """
        return self._order_reference_number

    @order_reference_number.setter
    def order_reference_number(self, order_reference_number):
        """Sets the order_reference_number of this OrderStatus.

        Client order number reference.  # noqa: E501

        :param order_reference_number: The order_reference_number of this OrderStatus.  # noqa: E501
        :type: str
        """

        self._order_reference_number = order_reference_number

    @property
    def status(self):
        """Gets the status of this OrderStatus.  # noqa: E501

        Indicates the Thibert status of the order  # noqa: E501

        :return: The status of this OrderStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderStatus.

        Indicates the Thibert status of the order  # noqa: E501

        :param status: The status of this OrderStatus.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(OrderStatus, dict):
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
        if not isinstance(other, OrderStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
