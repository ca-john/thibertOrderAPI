import csv
import json
import os
import requests
from datetime import datetime
from typing import Any, Dict, List, Union
import pprint
import six
import cred

HOST: str = cred.HOST
KEY: str = cred.KEY
JSON_URL: str = cred.JSON_URL
LOG_FILE: str = "order_log.csv"
TIMEOUT = 500    # seconds

ENDPOINT_DICT: Dict = {
    "order":
        "/api/Order",
    "tracking_number":
        "/api/Order/TrackingNumber",
    "order_status":
        "/api/Order/OrderStatus",
    "invoices":
        "/api/Order/Invoices",
    "invoice_pdf":
        "/api/Order/InvoicePDF",
    "vehicle_parts":
        "/api/FitmentThibert/VehicleParts/{SearchType}/{VehicleYear}/{VehicleMake}/{VehicleModel}"
}


class Contact(object):
    """A class to represent a contact.

    Do not edit the class manually.
    
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {'name': 'str', 'email': 'str', 'phone_number': 'str'}

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'phone_number': 'phoneNumber'
    }

    def __init__(self,
                 name=None,
                 email=None,
                 phone_number=None):    # noqa: E501
        """Contact - a model defined in Swagger."""
        self._name = None
        self._email = None
        self._phone_number = None
        self.discriminator = None
        self.name = name
        if email is not None:
            self.email = email
        self.phone_number = phone_number

    @property
    def name(self):
        """Get the name of this Contact.

        :return: The name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this Contact.

        :param name: The name of this Contact.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`")    # noqa: E501
        self._name = name

    @property
    def email(self):
        """Get the email of this Contact.

        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Set the email of this Contact.

        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """
        self._email = email

    @property
    def phone_number(self):
        """Get the phone_number of this Contact.

        :return: The phone_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Set the phone_number of this Contact.

        :param phone_number: The phone_number of this Contact.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError(
                "Invalid value for `phone_number`, must not be `None`"
            )    # noqa: E501

        self._phone_number = phone_number

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value
        if issubclass(Contact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class Address(object):
    """Class for Address.

    Do not edit the class manually.
    
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

    def __init__(self,
                 name=None,
                 address1=None,
                 address2=None,
                 zip_code=None,
                 city=None,
                 state=None,
                 country_code=None):    # noqa: E501
        """Address - a model defined in Swagger."""
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
        """Get the name of this Address.

        Name asssociated to the address.  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this Address.

        Name asssociated to the address.  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def address1(self):
        """Get the address1 of this Address.

        Number and street name combination.  # noqa: E501

        :return: The address1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Set the address1 of this Address.

        Number and street name combination.  # noqa: E501

        :param address1: The address1 of this Address.  # noqa: E501
        :type: str
        """
        self._address1 = address1

    @property
    def address2(self):
        """Get the address2 of this Address.

        Alternative number and street name combination.  # noqa: E501

        :return: The address2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Set the address2 of this Address.

        Alternative number and street name combination.  # noqa: E501

        :param address2: The address2 of this Address.  # noqa: E501
        :type: str
        """
        self._address2 = address2

    @property
    def zip_code(self):
        """Get the zip_code of this Address.

        AKA Postal code  # noqa: E501

        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Set the zip_code of this Address.

        AKA Postal code  # noqa: E501

        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type: str
        """
        self._zip_code = zip_code

    @property
    def city(self):
        """Get the city of this Address.

        Town associated with the address.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Set the city of this Address.

        Town associated with the address.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """Get the state of this Address.

        State or province depending on the country.  # noqa: E501

        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Set the state of this Address.

        State or province depending on the country.  # noqa: E501

        :param state: The state of this Address.  # noqa: E501
        :type: str
        """
        self._state = state

    @property
    def country_code(self):
        """Get the country_code of this Address.

        CA or USA  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Set the country_code of this Address.

        CA or USA  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        self._country_code = country_code

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value
        if issubclass(Address, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class OrderLine(object):
    """Class for order lines.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"thibert_part_number": "str", "quantity": "int"}

    attribute_map = {
        "thibert_part_number": "thibertPartNumber",
        "quantity": "quantity"
    }

    def __init__(self, thibert_part_number=None, quantity=None):    # noqa: E501
        """Orderline - a model defined in Swagger."""
        self._thibert_part_number = None
        self._quantity = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if quantity is not None:
            self.quantity = quantity

    @property
    def thibert_part_number(self):
        """Get the thibert_part_number of this OrderLine.

        Part number in the Thibert database.  # noqa: E501

        :return: The thibert_part_number of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Set the thibert_part_number of this OrderLine.

        Part number in the Thibert database.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this OrderLine.  # noqa: E501
        :type: str
        """
        self._thibert_part_number = thibert_part_number

    @property
    def quantity(self):
        """Get the quantity of this OrderLine.

        Quantity to ship.  # noqa: E501

        :return: The quantity of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Set the quantity of this OrderLine.

        Quantity to ship.  # noqa: E501

        :param quantity: The quantity of this OrderLine.  # noqa: E501
        :type: int
        """
        self._quantity = quantity

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    ))
            else:
                result[attr] = value
        if issubclass(OrderLine, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, OrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class Order(object):
    """Class for an order.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "order_reference_number": "str",
        "shipping_address": "Address",
        "contact_info": "Contact",
        "order_lines": "list[OrderLine]",
    }

    attribute_map = {
        "order_reference_number": "orderReferenceNumber",
        "shipping_address": "shippingAddress",
        "contact_info": "contactInfo",
        "order_lines": "orderLines",
    }

    def __init__(
        self,
        order_reference_number=None,
        shipping_address=None,
        contact_info=None,
        order_lines=None,
    ):    # noqa: E501
        """Order - a model defined in Swagger."""
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
        """Get the order_reference_number of this Order.

        User inputed for personnal reference.  # noqa: E501

        :return: The order_reference_number of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_reference_number

    @order_reference_number.setter
    def order_reference_number(self, order_reference_number):
        """Set the order_reference_number of this Order.

        User inputed for personnal reference.  # noqa: E501

        :param order_reference_number: The order_reference_number of this Order.  # noqa: E501
        :type: str
        """
        self._order_reference_number = order_reference_number

    @property
    def shipping_address(self):
        """Get the shipping_address of this Order.

        :return: The shipping_address of this Order.  # noqa: E501
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Set the shipping_address of this Order.

        :param shipping_address: The shipping_address of this Order.  # noqa: E501
        :type: Address
        """
        self._shipping_address = shipping_address

    @property
    def contact_info(self):
        """Get the contact_info of this Order.

        :return: The contact_info of this Order.  # noqa: E501
        :rtype: Contact
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Set the contact_info of this Order.

        :param contact_info: The contact_info of this Order.
        :type: Contact
        """
        self._contact_info = contact_info

    @property
    def order_lines(self):
        """Gets the order_lines of this Order.

        Parts in the order.  # noqa: E501

        :return: The order_lines of this Order.  # noqa: E501
        :rtype: list[OrderLine]
        """
        return self._order_lines

    @order_lines.setter
    def order_lines(self, order_lines):
        """Set the order_lines of this Order.

        Parts in the order.  # noqa: E501
        :param order_lines: The order_lines of this Order.  # noqa: E501
        :type: list[OrderLine]
        """
        self._order_lines = order_lines

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    ))
            else:
                result[attr] = value
        if issubclass(Order, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class APIConnector:
    """A base class for connecting to an API."""

    def __init__(self,
                 base_url: str = HOST,
                 api_key: str = KEY,
                 authorization: str = KEY):
        """Initialize the API connector.

        Args:
            base_url (str): Base URL for the API.
            api_key (str): The API key.
            authorization (str): Authorization header.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.authorization = authorization
        self.base_url = base_url

    def get_data(self, endpoint: str, params=None) -> Any:
        """Get data from the API.

        Args:
            endpoint (str): The url endpoint.
            params (Any, optional): Parameters to the endpoint. Defaults to None.

        Returns:
            Any: The response data.
        """
        url = self.base_url + endpoint
        headers = {
            "x-api-key": self.api_key,
            "Authorization": self.authorization
        }
        response = requests.get(url,
                                params=params,
                                headers=headers,
                                timeout=TIMEOUT)
        return response.json()

    def post_data(self, endpoint: str, data: Dict) -> Any:
        """Post data to the API.

        Args:
            endpoint (str): The endpoint.
            data (Dict): Data to be posted.

        Returns:
            Any: The response data.
        """
        url = self.base_url + endpoint
        headers = {
            "x-api-key": self.api_key,
            "Authorization": self.authorization,
            "Content-Type": "application/json"
        }
        response = requests.post(url,
                                 json=data,
                                 headers=headers,
                                 timeout=TIMEOUT)
        return response.json()


class CarLightingDistrictAPI(APIConnector):
    """The CarLightingDistrict API connector."""

    def __init__(self):
        """Create the CarLightingDistrict API connector."""
        super().__init__()

    def get_vehicle_years(self) -> Any:
        """Get a list of vehicle years.

        Returns:
            Any: Returns a list of vehicle years.
        """
        endpoint = "/api/CarLightingDistrict/Vehicle/Years"
        return self.get_data(endpoint)

    def get_vehicle_makes(self, vehicle_year: int) -> Any:
        """Get a list of vehicle makes for a given year."""
        endpoint = f"/api/CarLightingDistrict/Vehicle/Makes/{vehicle_year}"
        return self.get_data(endpoint)

    def get_vehicle_models(self, vehicle_year: int, vehicle_make: str) -> Any:
        """Get a list of vehicle models for a given year and make."""
        endpoint = (
            f"/api/CarLightingDistrict/Vehicle/Models/{vehicle_year}/{vehicle_make}"
        )
        return self.get_data(endpoint)


# class OrderAPI(APIConnector):
#     """The Order API connector."""

#     def __init__(self):
#         """Create Fthe Order API connector with default HOST and KEY."""
#         super().__init__()

#     def order(self, order_obj: Order) -> Any:
#         """Submit and order to the endpoint.

#         Args:
#             order (Dict): The order data. The schema is as follows

#             Canadian Orders:
#             {
#                             "orderReferenceNumber": "123456",
#                             "shippingAddress": {
#                                 "name": "Jean Hachette",
#                                 "address1": "200, Blvd St-Jean-Baptiste",
#                                 "address2": "",
#                                 "zipCode": "J6R 2L2",
#                                 "city": "Mercier",
#                                 "state": "QC",
#                                 "countryCode": "CA"
#                             },
#                             "contactInfo": {
#                                 "name": "Jean Hachette",
#                                 "email": "noreply@rthibert.com",
#                                 "phoneNumber": "5149999999"
#                             },
#                             "orderLines": [
#                                 {
#                                 "thibertPartNumber": "081001",
#                                 "quantity": 4
#                                 },
#                                 {
#                                 "thibertPartNumber": "WT4710121",
#                                 "quantity": 1
#                                 }
#                             ]
#             }

#             US Orders:
#             {
#                                 "orderReferenceNumber": "123456",
#                                 "shippingAddress": {
#                                         "name": "Bob Builder",
#                                         "address1": "90 Trade Zone Court",
#                                         "address2": "",
#                                         "zipCode": "11779",
#                                         "city": "Ronkonkoma",
#                                         "state": "NY",
#                                         "countryCode": "US"
#                                 },
#                                 "contactInfo": {
#                                         "name": "Bob Builder",
#                                         "email": "noreply@rthibert.com",
#                                         "phoneNumber": "+1 619-999-9999"
#                                 },
#                                 "orderLines": [
#                                         {
#                                         "thibertPartNumber": "081001",
#                                         "quantity": 4
#                                         },
#                                         {
#                                         "thibertPartNumber": "WT4710121",
#                                         "quantity": 1
#                                         }
#                                 ]
#             }
#         Returns:
#             Any: The response data.
#         """
#         # Get the endpoint from the dictionary.
#         endpoint = ENDPOINT_DICT["order"]
#         self.post_data(endpoint, data=json.dumps(order_obj.to_dict()))

#         return ""

#     def tracking_number(self, tracking_number: str) -> Any:
#         """Get the tracking information for a given tracking number.

#         Args:
#             tracking_number (str): The tracking number.
#         Returns:
#             Any: The response data.
#         """
#         # Get the endpoint from the dictionary.
#         endpoint = ENDPOINT_DICT["tracking_number"]
#         return self.get_data(endpoint, params=tracking_number)


class OrderApi(object):
    """DO NOT EDIT THIS CLASS
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_order_invoice_pdf_get(self, **kwargs):    # noqa: E501
        """Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller's side.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoice_pdf_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: Invoice number
        :param str original_order_id: Order number related to the specified invoice
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_invoice_pdf_get_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_invoice_pdf_get_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_invoice_pdf_get_with_http_info(self,
                                                 **kwargs):    # noqa: E501
        """Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller's side.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoice_pdf_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: Invoice number
        :param str original_order_id: Order number related to the specified invoice
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id', 'original_order_id']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method api_order_invoice_pdf_get" % key)
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'invoice_id' in params:
            query_params.append(
                ('invoiceId', params['invoice_id']))    # noqa: E501
        if 'original_order_id' in params:
            query_params.append(('originalOrderId',
                                 params['original_order_id']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/InvoicePDF',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_invoices_get(self, **kwargs):    # noqa: E501
        """Retrieves invoices associated to the account in pages of 10.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoices_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start_date: Filter invoices by start date
        :param datetime end_date: Filter invoices by end date
        :param int page: Page to retrieve
        :return: list[Invoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_invoices_get_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_invoices_get_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_invoices_get_with_http_info(self, **kwargs):    # noqa: E501
        """Retrieves invoices associated to the account in pages of 10.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoices_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start_date: Filter invoices by start date
        :param datetime end_date: Filter invoices by end date
        :param int page: Page to retrieve
        :return: list[Invoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'page']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_invoices_get")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(
                ('startDate', params['start_date']))    # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))    # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/Invoices',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Invoice]',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_order_status_post(self, **kwargs):    # noqa: E501
        """Retrieve the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_order_status_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)
        :param int page_number: Number of the page to retrieve. Default value: 1
        :param int page_size: Number of results per page. Default value: 50, Maximum allowed: 200
        :return: list[OrderStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_order_status_post_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_order_status_post_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_order_status_post_with_http_info(self,
                                                   **kwargs):    # noqa: E501
        """Retrieve the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_order_status_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)
        :param int page_number: Number of the page to retrieve. Default value: 1
        :param int page_size: Number of results per page. Default value: 50, Maximum allowed: 200
        :return: list[OrderStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['body', 'order_number_type', 'page_number',
                      'page_size']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_order_status_post")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number_type' in params:
            query_params.append(('OrderNumberType',
                                 params['order_number_type']))    # noqa: E501
        if 'page_number' in params:
            query_params.append(
                ('PageNumber', params['page_number']))    # noqa: E501
        if 'page_size' in params:
            query_params.append(
                ('PageSize', params['page_size']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(    # noqa: E501
                ['application/json', 'text/json',
                 'application/*+json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/OrderStatus',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OrderStatus]',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_post(self, **kwargs):    # noqa: E501
        """Process an order in our systems.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Order body: Order to be saved.
        :return: OrderConfirmation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_post_with_http_info(**kwargs)    # noqa: E501
        (data
        ) = self.api_order_post_with_http_info(**kwargs)    # noqa: E501
        return data

    def api_order_post_with_http_info(self, **kwargs):    # noqa: E501
        """Process an order in our systems.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Order body: Order to be saved.
        :return: OrderConfirmation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_post")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(    # noqa: E501
                ['application/json', 'text/json',
                 'application/*+json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderConfirmation',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_tracking_number_post(self, **kwargs):    # noqa: E501
        """Retrieve the tracking numbers associated with the specified orders.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_tracking_number_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType.
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)
        :return: list[OrderTracking]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_tracking_number_post_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_tracking_number_post_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_tracking_number_post_with_http_info(self,
                                                      **kwargs):    # noqa: E501
        """Retrieve the tracking numbers associated with the specified orders.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_tracking_number_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType.
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)
        :return: list[OrderTracking]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['body', 'order_number_type']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_tracking_number_post")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number_type' in params:
            query_params.append(('OrderNumberType',
                                 params['order_number_type']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(    # noqa: E501
                ['application/json', 'text/json',
                 'application/*+json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/TrackingNumber',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OrderTracking]',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


def get_paths(url: str = JSON_URL) -> Dict[str, Dict]:
    """Get the paths from the OpenAPI JSON file.

    Args:
        url (str, optional): The url to the JSON specification file. Defaults to JSON_URL.

    Returns:
        Dict[str, Dict]: Return the paths from the JSON file.
    """
    response = requests.get(url, timeout=500).text
    response_info = json.loads(response)
    print(f"Connected to OpenAPI ver {response_info.get('openapi')}")
    if response_info.get("paths") is None:
        print("No paths found.")
    return response_info.get("paths")


def write_order_log(order_number: str,
                    order_date: str,
                    filename: str = LOG_FILE) -> None:
    """Write order the log to the log file, if it exists. Create the file if it does not.

    Args:
        filename (str, optional): The file name of the log file. Defaults to LOG_FILE.
        order_number (str): The order number.
        order_date (str): The order date.
    """
    # Check if the file exists and create if it doesn't, including the header
    header = ["Log time", "Order Creation Date", "Order Number"]
    if not os.path.exists(filename):
        # Create the file
        with open(filename, "a+", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
        file.close()

    # Write the data to the file
    with open(filename, "a+", encoding="utf-8") as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
        row = [timestamp, order_date, order_number]
        writer.writerow(row)

    # Close the file
    file.close()


def main():
    """Start the main entry point of the app.
    
    This is where we get the input from the user and create the order and submit it.
    """
    # api = CarLightingDistrictAPI()

    # # Example usage
    # years = api.get_vehicle_years()
    # print("Years:", years)

    # Check the paths
    paths = get_paths()
    assert paths is not None
    assert len(paths) > 0

    # if years:
    #     makes = api.get_vehicle_makes(years[0])
    #     print("Makes for the first year:", makes)

    #     if makes:
    #         models = api.get_vehicle_models(years[0], makes[0])
    #         print(f"Models for {years[0]} and {makes[0]}:", models)
    # write_order_log("123456", "2021-01-01")

    print("Thibert Order API\n")

    ref_number: str = input("Enter the order reference number: ")
    customer_name: str = input("Enter the customer name: ")
    customer_shipping_address1: str = input("Enter shipping address1: ")
    customer_shipping_address2: str = input(
        "Enter shipping address2, press enter if empty: ")
    customer_zip_code: str = input("Enter the zip code: ")
    customer_city: str = input("Enter the city: ")
    customer_state: str = input("Enter the state: ")
    country_code: str = input("Enter the country code: ")

    contact_name: str = input("Enter the contact name: ")
    contact_email: str = input("Enter the contact email: ")
    contact_phone_number: str = input("Enter the contact phone number: ")

    order_lines: List[OrderLine] = []
    print("Order Line - Enter the part number and quantity for each part:")
    print(" ")
    while True:
        part_number = input("Enter the part number: ")
        quantity = input("Enter the quantity: ")
        if not (part_number and quantity):
            print("Part number and quantity are required.")
            continue
        if not quantity.isdigit():
            print("Quantity must be a number.")
            continue
        # order_lines.append({
        #     "thibertPartNumber": part_number,
        #     "quantity": int(quantity)
        # })

        line_item = OrderLine()
        line_item.thibert_part_number = part_number
        line_item.quantity = int(quantity)
        order_lines.append(line_item)

        if input("Add another part? (y/n): ") == "n":
            break

    # Contact for the order
    contact = Contact(name=contact_name,
                      email=contact_email,
                      phone_number=contact_phone_number)
    # contact.name = contact_name
    # contact.email = contact_email
    # contact.phone_number = contact_phone_number

    # Customer for the order
    customer_address = Address(name=customer_name,
                               address1=customer_shipping_address1,
                               address2=customer_shipping_address2,
                               zip_code=customer_zip_code,
                               city=customer_city,
                               state=customer_state,
                               country_code=country_code)
    # customer_address.name = customer_name
    # customer_address.address1 = customer_shipping_address1
    # customer_address.address2 = customer_shipping_address2
    # customer_address.zip_code = customer_zip_code
    # customer_address.city = customer_city
    # customer_address.state = customer_state
    # customer_address.country_code = country_code
    order_obj = Order(order_reference_number=ref_number,
                      contact_info=contact,
                      shipping_address=customer_address,
                      order_lines=order_lines)
    # order_obj.order_reference_number = ref_number
    # order_obj.contact_info = contact
    # order_obj.shipping_address = customer_address

    order = OrderAPI()

    #order.order(order_obj)

    print(order_obj.to_str())
    print(
        "---CONFIRM THAT THE INFORMATION IS CORRECT BEFORE SUBMITTING THE ORDER.---"
    )

    if input("Submit the order? (y/n): ") == "y":
        print("Submitting the order...")
    else:
        print("Cancelled - Order not submitted.")


if __name__ == "__main__":
    main()
