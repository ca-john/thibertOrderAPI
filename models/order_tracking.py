# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class OrderTracking(object):
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
        'web_order_reference': 'str',
        'tracking_number': 'str',
        'tracking_url': 'str',
        'carrier': 'str',
        'thibert_part_number': 'str',
        'shiped_quantity': 'int'
    }

    attribute_map = {
        'thibert_order_number': 'thibertOrderNumber',
        'web_order_reference': 'webOrderReference',
        'tracking_number': 'trackingNumber',
        'tracking_url': 'trackingURL',
        'carrier': 'carrier',
        'thibert_part_number': 'thibertPartNumber',
        'shiped_quantity': 'shipedQuantity'
    }

    def __init__(self, thibert_order_number=None, web_order_reference=None, tracking_number=None, tracking_url=None, carrier=None, thibert_part_number=None, shiped_quantity=None):  # noqa: E501
        """OrderTracking - a model defined in Swagger"""  # noqa: E501
        self._thibert_order_number = None
        self._web_order_reference = None
        self._tracking_number = None
        self._tracking_url = None
        self._carrier = None
        self._thibert_part_number = None
        self._shiped_quantity = None
        self.discriminator = None
        if thibert_order_number is not None:
            self.thibert_order_number = thibert_order_number
        if web_order_reference is not None:
            self.web_order_reference = web_order_reference
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if carrier is not None:
            self.carrier = carrier
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if shiped_quantity is not None:
            self.shiped_quantity = shiped_quantity

    @property
    def thibert_order_number(self):
        """Gets the thibert_order_number of this OrderTracking.  # noqa: E501


        :return: The thibert_order_number of this OrderTracking.  # noqa: E501
        :rtype: str
        """
        return self._thibert_order_number

    @thibert_order_number.setter
    def thibert_order_number(self, thibert_order_number):
        """Sets the thibert_order_number of this OrderTracking.


        :param thibert_order_number: The thibert_order_number of this OrderTracking.  # noqa: E501
        :type: str
        """

        self._thibert_order_number = thibert_order_number

    @property
    def web_order_reference(self):
        """Gets the web_order_reference of this OrderTracking.  # noqa: E501


        :return: The web_order_reference of this OrderTracking.  # noqa: E501
        :rtype: str
        """
        return self._web_order_reference

    @web_order_reference.setter
    def web_order_reference(self, web_order_reference):
        """Sets the web_order_reference of this OrderTracking.


        :param web_order_reference: The web_order_reference of this OrderTracking.  # noqa: E501
        :type: str
        """

        self._web_order_reference = web_order_reference

    @property
    def tracking_number(self):
        """Gets the tracking_number of this OrderTracking.  # noqa: E501


        :return: The tracking_number of this OrderTracking.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this OrderTracking.


        :param tracking_number: The tracking_number of this OrderTracking.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

    @property
    def tracking_url(self):
        """Gets the tracking_url of this OrderTracking.  # noqa: E501


        :return: The tracking_url of this OrderTracking.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this OrderTracking.


        :param tracking_url: The tracking_url of this OrderTracking.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def carrier(self):
        """Gets the carrier of this OrderTracking.  # noqa: E501


        :return: The carrier of this OrderTracking.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this OrderTracking.


        :param carrier: The carrier of this OrderTracking.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this OrderTracking.  # noqa: E501


        :return: The thibert_part_number of this OrderTracking.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this OrderTracking.


        :param thibert_part_number: The thibert_part_number of this OrderTracking.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def shiped_quantity(self):
        """Gets the shiped_quantity of this OrderTracking.  # noqa: E501


        :return: The shiped_quantity of this OrderTracking.  # noqa: E501
        :rtype: int
        """
        return self._shiped_quantity

    @shiped_quantity.setter
    def shiped_quantity(self, shiped_quantity):
        """Sets the shiped_quantity of this OrderTracking.


        :param shiped_quantity: The shiped_quantity of this OrderTracking.  # noqa: E501
        :type: int
        """

        self._shiped_quantity = shiped_quantity

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
        if issubclass(OrderTracking, dict):
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
        if not isinstance(other, OrderTracking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
