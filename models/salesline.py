# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class Salesline(object):
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
        'line_no': 'int',
        'product_id': 'str',
        'variant_id': 'str',
        'product_title': 'str',
        'title': 'str',
        'quantity': 'int',
        'price': 'float',
        'tax_percent': 'float',
        'inventory': 'int',
        'line_amount': 'float',
        'parent_line_no': 'int',
        'is_read_only_line': 'int',
        'line_type': 'str',
        'unit_of_measure_id': 'str',
        'unit_of_measure_description': 'str',
        'shipment_date': 'str',
        'quantity_shipped': 'int',
        'quantity_invoiced': 'int',
        'quantity_outstanding': 'int',
        'service_charge_id': 'str'
    }

    attribute_map = {
        'line_no': 'lineNo',
        'product_id': 'productId',
        'variant_id': 'variantId',
        'product_title': 'productTitle',
        'title': 'title',
        'quantity': 'quantity',
        'price': 'price',
        'tax_percent': 'taxPercent',
        'inventory': 'inventory',
        'line_amount': 'lineAmount',
        'parent_line_no': 'parentLineNo',
        'is_read_only_line': 'isReadOnlyLine',
        'line_type': 'lineType',
        'unit_of_measure_id': 'unitOfMeasureId',
        'unit_of_measure_description': 'unitOfMeasureDescription',
        'shipment_date': 'shipmentDate',
        'quantity_shipped': 'quantityShipped',
        'quantity_invoiced': 'quantityInvoiced',
        'quantity_outstanding': 'quantityOutstanding',
        'service_charge_id': 'serviceChargeId'
    }

    def __init__(self, line_no=None, product_id=None, variant_id=None, product_title=None, title=None, quantity=None, price=None, tax_percent=None, inventory=None, line_amount=None, parent_line_no=None, is_read_only_line=None, line_type=None, unit_of_measure_id=None, unit_of_measure_description=None, shipment_date=None, quantity_shipped=None, quantity_invoiced=None, quantity_outstanding=None, service_charge_id=None):  # noqa: E501
        """Salesline - a model defined in Swagger"""  # noqa: E501
        self._line_no = None
        self._product_id = None
        self._variant_id = None
        self._product_title = None
        self._title = None
        self._quantity = None
        self._price = None
        self._tax_percent = None
        self._inventory = None
        self._line_amount = None
        self._parent_line_no = None
        self._is_read_only_line = None
        self._line_type = None
        self._unit_of_measure_id = None
        self._unit_of_measure_description = None
        self._shipment_date = None
        self._quantity_shipped = None
        self._quantity_invoiced = None
        self._quantity_outstanding = None
        self._service_charge_id = None
        self.discriminator = None
        if line_no is not None:
            self.line_no = line_no
        if product_id is not None:
            self.product_id = product_id
        if variant_id is not None:
            self.variant_id = variant_id
        if product_title is not None:
            self.product_title = product_title
        if title is not None:
            self.title = title
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if tax_percent is not None:
            self.tax_percent = tax_percent
        if inventory is not None:
            self.inventory = inventory
        if line_amount is not None:
            self.line_amount = line_amount
        if parent_line_no is not None:
            self.parent_line_no = parent_line_no
        if is_read_only_line is not None:
            self.is_read_only_line = is_read_only_line
        if line_type is not None:
            self.line_type = line_type
        if unit_of_measure_id is not None:
            self.unit_of_measure_id = unit_of_measure_id
        if unit_of_measure_description is not None:
            self.unit_of_measure_description = unit_of_measure_description
        if shipment_date is not None:
            self.shipment_date = shipment_date
        if quantity_shipped is not None:
            self.quantity_shipped = quantity_shipped
        if quantity_invoiced is not None:
            self.quantity_invoiced = quantity_invoiced
        if quantity_outstanding is not None:
            self.quantity_outstanding = quantity_outstanding
        if service_charge_id is not None:
            self.service_charge_id = service_charge_id

    @property
    def line_no(self):
        """Gets the line_no of this Salesline.  # noqa: E501


        :return: The line_no of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._line_no

    @line_no.setter
    def line_no(self, line_no):
        """Sets the line_no of this Salesline.


        :param line_no: The line_no of this Salesline.  # noqa: E501
        :type: int
        """

        self._line_no = line_no

    @property
    def product_id(self):
        """Gets the product_id of this Salesline.  # noqa: E501


        :return: The product_id of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Salesline.


        :param product_id: The product_id of this Salesline.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def variant_id(self):
        """Gets the variant_id of this Salesline.  # noqa: E501


        :return: The variant_id of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._variant_id

    @variant_id.setter
    def variant_id(self, variant_id):
        """Sets the variant_id of this Salesline.


        :param variant_id: The variant_id of this Salesline.  # noqa: E501
        :type: str
        """

        self._variant_id = variant_id

    @property
    def product_title(self):
        """Gets the product_title of this Salesline.  # noqa: E501


        :return: The product_title of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._product_title

    @product_title.setter
    def product_title(self, product_title):
        """Sets the product_title of this Salesline.


        :param product_title: The product_title of this Salesline.  # noqa: E501
        :type: str
        """

        self._product_title = product_title

    @property
    def title(self):
        """Gets the title of this Salesline.  # noqa: E501


        :return: The title of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Salesline.


        :param title: The title of this Salesline.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def quantity(self):
        """Gets the quantity of this Salesline.  # noqa: E501


        :return: The quantity of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Salesline.


        :param quantity: The quantity of this Salesline.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this Salesline.  # noqa: E501


        :return: The price of this Salesline.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Salesline.


        :param price: The price of this Salesline.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def tax_percent(self):
        """Gets the tax_percent of this Salesline.  # noqa: E501


        :return: The tax_percent of this Salesline.  # noqa: E501
        :rtype: float
        """
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, tax_percent):
        """Sets the tax_percent of this Salesline.


        :param tax_percent: The tax_percent of this Salesline.  # noqa: E501
        :type: float
        """

        self._tax_percent = tax_percent

    @property
    def inventory(self):
        """Gets the inventory of this Salesline.  # noqa: E501


        :return: The inventory of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this Salesline.


        :param inventory: The inventory of this Salesline.  # noqa: E501
        :type: int
        """

        self._inventory = inventory

    @property
    def line_amount(self):
        """Gets the line_amount of this Salesline.  # noqa: E501


        :return: The line_amount of this Salesline.  # noqa: E501
        :rtype: float
        """
        return self._line_amount

    @line_amount.setter
    def line_amount(self, line_amount):
        """Sets the line_amount of this Salesline.


        :param line_amount: The line_amount of this Salesline.  # noqa: E501
        :type: float
        """

        self._line_amount = line_amount

    @property
    def parent_line_no(self):
        """Gets the parent_line_no of this Salesline.  # noqa: E501


        :return: The parent_line_no of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._parent_line_no

    @parent_line_no.setter
    def parent_line_no(self, parent_line_no):
        """Sets the parent_line_no of this Salesline.


        :param parent_line_no: The parent_line_no of this Salesline.  # noqa: E501
        :type: int
        """

        self._parent_line_no = parent_line_no

    @property
    def is_read_only_line(self):
        """Gets the is_read_only_line of this Salesline.  # noqa: E501


        :return: The is_read_only_line of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._is_read_only_line

    @is_read_only_line.setter
    def is_read_only_line(self, is_read_only_line):
        """Sets the is_read_only_line of this Salesline.


        :param is_read_only_line: The is_read_only_line of this Salesline.  # noqa: E501
        :type: int
        """

        self._is_read_only_line = is_read_only_line

    @property
    def line_type(self):
        """Gets the line_type of this Salesline.  # noqa: E501


        :return: The line_type of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._line_type

    @line_type.setter
    def line_type(self, line_type):
        """Sets the line_type of this Salesline.


        :param line_type: The line_type of this Salesline.  # noqa: E501
        :type: str
        """

        self._line_type = line_type

    @property
    def unit_of_measure_id(self):
        """Gets the unit_of_measure_id of this Salesline.  # noqa: E501


        :return: The unit_of_measure_id of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure_id

    @unit_of_measure_id.setter
    def unit_of_measure_id(self, unit_of_measure_id):
        """Sets the unit_of_measure_id of this Salesline.


        :param unit_of_measure_id: The unit_of_measure_id of this Salesline.  # noqa: E501
        :type: str
        """

        self._unit_of_measure_id = unit_of_measure_id

    @property
    def unit_of_measure_description(self):
        """Gets the unit_of_measure_description of this Salesline.  # noqa: E501


        :return: The unit_of_measure_description of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure_description

    @unit_of_measure_description.setter
    def unit_of_measure_description(self, unit_of_measure_description):
        """Sets the unit_of_measure_description of this Salesline.


        :param unit_of_measure_description: The unit_of_measure_description of this Salesline.  # noqa: E501
        :type: str
        """

        self._unit_of_measure_description = unit_of_measure_description

    @property
    def shipment_date(self):
        """Gets the shipment_date of this Salesline.  # noqa: E501


        :return: The shipment_date of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, shipment_date):
        """Sets the shipment_date of this Salesline.


        :param shipment_date: The shipment_date of this Salesline.  # noqa: E501
        :type: str
        """

        self._shipment_date = shipment_date

    @property
    def quantity_shipped(self):
        """Gets the quantity_shipped of this Salesline.  # noqa: E501


        :return: The quantity_shipped of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._quantity_shipped

    @quantity_shipped.setter
    def quantity_shipped(self, quantity_shipped):
        """Sets the quantity_shipped of this Salesline.


        :param quantity_shipped: The quantity_shipped of this Salesline.  # noqa: E501
        :type: int
        """

        self._quantity_shipped = quantity_shipped

    @property
    def quantity_invoiced(self):
        """Gets the quantity_invoiced of this Salesline.  # noqa: E501


        :return: The quantity_invoiced of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._quantity_invoiced

    @quantity_invoiced.setter
    def quantity_invoiced(self, quantity_invoiced):
        """Sets the quantity_invoiced of this Salesline.


        :param quantity_invoiced: The quantity_invoiced of this Salesline.  # noqa: E501
        :type: int
        """

        self._quantity_invoiced = quantity_invoiced

    @property
    def quantity_outstanding(self):
        """Gets the quantity_outstanding of this Salesline.  # noqa: E501


        :return: The quantity_outstanding of this Salesline.  # noqa: E501
        :rtype: int
        """
        return self._quantity_outstanding

    @quantity_outstanding.setter
    def quantity_outstanding(self, quantity_outstanding):
        """Sets the quantity_outstanding of this Salesline.


        :param quantity_outstanding: The quantity_outstanding of this Salesline.  # noqa: E501
        :type: int
        """

        self._quantity_outstanding = quantity_outstanding

    @property
    def service_charge_id(self):
        """Gets the service_charge_id of this Salesline.  # noqa: E501


        :return: The service_charge_id of this Salesline.  # noqa: E501
        :rtype: str
        """
        return self._service_charge_id

    @service_charge_id.setter
    def service_charge_id(self, service_charge_id):
        """Sets the service_charge_id of this Salesline.


        :param service_charge_id: The service_charge_id of this Salesline.  # noqa: E501
        :type: str
        """

        self._service_charge_id = service_charge_id

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
        if issubclass(Salesline, dict):
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
        if not isinstance(other, Salesline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
