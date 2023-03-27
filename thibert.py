import csv
import json
import os
import requests
from datetime import datetime
from typing import Any, Dict, List, Union
import pprint
import re
import six
import cred


HOST: str = cred.HOST
KEY: str = cred.KEY
JSON_URL: str = cred.JSON_URL
LOG_FILE: str = "order_log.csv"


ENDPOINT_DICT: Dict = {
    "order": "/api/Order",
    "tracking_number": "/api/Order/TrackingNumber",
    "order_status": "/api/Order/OrderStatus",
    "invoices": "/api/Order/Invoices",
    "invoice_pdf": "/api/Order/InvoicePDF",
}







class OrderLine(object):
    """ Class for order lines.  # noqa: E501
    
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    
    swagger_types = {
        'thibert_part_number': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'quantity': 'quantity'
    }

    def __init__(self, thibert_part_number=None, quantity=None):  # noqa: E501
        """OrderLine - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._quantity = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if quantity is not None:
            self.quantity = quantity

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this OrderLine.  # noqa: E501

        Part number in the Thibert database.  # noqa: E501

        :return: The thibert_part_number of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this OrderLine.

        Part number in the Thibert database.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this OrderLine.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def quantity(self):
        """Gets the quantity of this OrderLine.  # noqa: E501

        Quantity to ship.  # noqa: E501

        :return: The quantity of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderLine.

        Quantity to ship.  # noqa: E501

        :param quantity: The quantity of this OrderLine.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(OrderLine, dict):
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
        if not isinstance(other, OrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other









class Order(object):
    """Class for an order.  # noqa: E501

    Do not edit the class manually.
    
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

    def __init__(self, order_reference_number=None,
                 shipping_address=None, contact_info=None, order_lines=None):  # noqa: E501
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














class APIConnector:
    """A base class for connecting to an API."""

    def __init__(
        self, base_url: str = HOST, api_key: str = KEY, authorization: str = KEY
    ):
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
        headers = {"x-api-key": self.api_key, "Authorization": self.authorization}
        response = requests.get(url, params=params, headers=headers)
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


class OrderAPI(APIConnector):
    """The Order API connector."""

    def __init__(self):
        """Create Fthe Order API connector with default HOST and KEY."""
        super().__init__()

    def order(self, order: Dict[str, Union[str, Dict[str, Union[str, int]]]]) -> Any:
        """Submit and order to the endpoint.

        Args:
            order (Dict): The order data. The schema is as follows

            Canadian Orders:
            {
                            "orderReferenceNumber": "123456",
                            "shippingAddress": {
                                "name": "Jean Hachette",
                                "address1": "200, Blvd St-Jean-Baptiste",
                                "address2": "",
                                "zipCode": "J6R 2L2",
                                "city": "Mercier",
                                "state": "QC",
                                "countryCode": "CA"
                            },
                            "contactInfo": {
                                "name": "Jean Hachette",
                                "email": "noreply@rthibert.com",
                                "phoneNumber": "5149999999"
                            },
                            "orderLines": [
                                {
                                "thibertPartNumber": "081001",
                                "quantity": 4
                                },
                                {
                                "thibertPartNumber": "WT4710121",
                                "quantity": 1
                                }
                            ]
            }

            US Orders:
            {
                                "orderReferenceNumber": "123456",
                                "shippingAddress": {
                                        "name": "Bob Builder",
                                        "address1": "90 Trade Zone Court",
                                        "address2": "",
                                        "zipCode": "11779",
                                        "city": "Ronkonkoma",
                                        "state": "NY",
                                        "countryCode": "US"
                                },
                                "contactInfo": {
                                        "name": "Bob Builder",
                                        "email": "noreply@rthibert.com",
                                        "phoneNumber": "+1 619-999-9999"
                                },
                                "orderLines": [
                                        {
                                        "thibertPartNumber": "081001",
                                        "quantity": 4
                                        },
                                        {
                                        "thibertPartNumber": "WT4710121",
                                        "quantity": 1
                                        }
                                ]
            }
        Returns:
            Any: The response data.
        """
        # Get the endpoint from the dictionary.
        endpoint = ENDPOINT_DICT["order"]
        self.get_data(endpoint, params=order)

        return ""

    def tracking_number(self, tracking_number: str) -> Any:
        """Get the tracking information for a given tracking number.

        Args:
            tracking_number (str): The tracking number.
        Returns:
            Any: The response data.
        """
        # Get the endpoint from the dictionary.
        endpoint = ENDPOINT_DICT["tracking_number"]
        return self.get_data(endpoint, params=tracking_number)


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


def write_order_log(order_number: str, order_date: str, filename: str = LOG_FILE) -> None:
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
    """Start the main entry point of the app."""
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
    write_order_log("123456", "2021-01-01")
    
    
    
    print("Thibert Order API\n")
    
    ref_number: str = input("Enter the order reference number: ")
    customer_name: str = input("Enter the customer name: ")
    customer_shipping_address1: str = input("Enter shipping address1: ")
    customer_shipping_address2: str = input("Enter shipping address2, press enter if empty: ")
    customer_zip_code: str = input("Enter the zip code: ")
    customer_city: str = input("Enter the city: ")
    customer_state: str = input("Enter the state: ")
    country_code: str = input("Enter the country code: ")
    
    contact_name: str = input("Enter the contact name: ")
    contact_email: str = input("Enter the contact email: ")
    contact_phone_number: str = input("Enter the contact phone number: ")
    
    order_lines: List[Dict[str, Union[str, int]]] = []
    
    while(True):
        part_number = input("Enter the part number: ")
        quantity = input("Enter the quantity: ")
        if not (part_number and quantity):
            print("Part number and quantity are required.")
            continue
        if not quantity.isdigit():
            print("Quantity must be a number.")
            continue
        order_lines.append({"thibertPartNumber": part_number, "quantity": int(quantity)})
        if input("Add another part? (y/n): ") == "n":
            break
    
    
    
    
    order_obj = Order()
    order_obj.order_lines = order_lines
    
    
    
    order_dict = {
        "orderReferenceNumber": ref_number,
        "shippingAddress": {
            "name": customer_name,
            "address1": customer_shipping_address1,
            "address2": customer_shipping_address2,
            "zipCode": customer_zip_code,
            "city": customer_city,
            "state": customer_state,
            "countryCode": country_code
        },
        "contactInfo": {
            "name": contact_name,
            "email": contact_email,
            "phoneNumber": contact_phone_number
        },
        
        
    }
    

if __name__ == "__main__":
    main()
