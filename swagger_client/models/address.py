# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class Address(object):
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
        'name': 'str',
        'address1': 'str',
        'address2': 'str',
        'zip_code': 'str',
        'city': 'str',
        'state': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address1': 'address1',
        'address2': 'address2',
        'zip_code': 'zipCode',
        'city': 'city',
        'state': 'state',
        'country_code': 'countryCode'
    }

    def __init__(self, name=None, address1=None, address2=None, zip_code=None, city=None, state=None, country_code=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._address1 = None
        self._address2 = None
        self._zip_code = None
        self._city = None
        self._state = None
        self._country_code = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country_code is not None:
            self.country_code = country_code

    @property
    def name(self):
        """Gets the name of this Address.  # noqa: E501

        Name asssociated to the address.  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Address.

        Name asssociated to the address.  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address1(self):
        """Gets the address1 of this Address.  # noqa: E501

        Number and street name combination.  # noqa: E501

        :return: The address1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Address.

        Number and street name combination.  # noqa: E501

        :param address1: The address1 of this Address.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Address.  # noqa: E501

        Alternative number and street name combination.  # noqa: E501

        :return: The address2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Address.

        Alternative number and street name combination.  # noqa: E501

        :param address2: The address2 of this Address.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def zip_code(self):
        """Gets the zip_code of this Address.  # noqa: E501

        AKA Postal code  # noqa: E501

        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Address.

        AKA Postal code  # noqa: E501

        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        Town associated with the address.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        Town associated with the address.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501

        State or province depending on the country.  # noqa: E501

        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.

        State or province depending on the country.  # noqa: E501

        :param state: The state of this Address.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501

        CA or USA  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.

        CA or USA  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
