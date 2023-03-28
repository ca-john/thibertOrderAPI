# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class Order(object):
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
        'order_reference_number': 'str',
        'shipping_address': 'Address',
        'contact_info': 'Contact',
        'order_lines': 'list[OrderLine]'
    }

    attribute_map = {
        'order_reference_number': 'orderReferenceNumber',
        'shipping_address': 'shippingAddress',
        'contact_info': 'contactInfo',
        'order_lines': 'orderLines'
    }

    def __init__(self, order_reference_number=None, shipping_address=None, contact_info=None, order_lines=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._order_reference_number = None
        self._shipping_address = None
        self._contact_info = None
        self._order_lines = None
        self.discriminator = None
        if order_reference_number is not None:
            self.order_reference_number = order_reference_number
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if contact_info is not None:
            self.contact_info = contact_info
        if order_lines is not None:
            self.order_lines = order_lines

    @property
    def order_reference_number(self):
        """Gets the order_reference_number of this Order.  # noqa: E501

        User inputed for personnal reference.  # noqa: E501

        :return: The order_reference_number of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_reference_number

    @order_reference_number.setter
    def order_reference_number(self, order_reference_number):
        """Sets the order_reference_number of this Order.

        User inputed for personnal reference.  # noqa: E501

        :param order_reference_number: The order_reference_number of this Order.  # noqa: E501
        :type: str
        """

        self._order_reference_number = order_reference_number

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Order.  # noqa: E501


        :return: The shipping_address of this Order.  # noqa: E501
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Order.


        :param shipping_address: The shipping_address of this Order.  # noqa: E501
        :type: Address
        """

        self._shipping_address = shipping_address

    @property
    def contact_info(self):
        """Gets the contact_info of this Order.  # noqa: E501


        :return: The contact_info of this Order.  # noqa: E501
        :rtype: Contact
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this Order.


        :param contact_info: The contact_info of this Order.  # noqa: E501
        :type: Contact
        """

        self._contact_info = contact_info

    @property
    def order_lines(self):
        """Gets the order_lines of this Order.  # noqa: E501

        Parts in the order.  # noqa: E501

        :return: The order_lines of this Order.  # noqa: E501
        :rtype: list[OrderLine]
        """
        return self._order_lines

    @order_lines.setter
    def order_lines(self, order_lines):
        """Sets the order_lines of this Order.

        Parts in the order.  # noqa: E501

        :param order_lines: The order_lines of this Order.  # noqa: E501
        :type: list[OrderLine]
        """

        self._order_lines = order_lines

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
