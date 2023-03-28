# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class WheelInstallationPart(object):
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
        'bolt_per_wheel_qty': 'str',
        'innerpack': 'int',
        'qty_per_wheel': 'int',
        'sort_order': 'int',
        'installation_part_type': 'list[LocalizedString]',
        'part': 'Part',
        'compatible_keys': 'list[Part]'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'bolt_per_wheel_qty': 'boltPerWheelQty',
        'innerpack': 'innerpack',
        'qty_per_wheel': 'qtyPerWheel',
        'sort_order': 'sortOrder',
        'installation_part_type': 'installationPartType',
        'part': 'part',
        'compatible_keys': 'compatibleKeys'
    }

    def __init__(self, thibert_part_number=None, bolt_per_wheel_qty=None, innerpack=None, qty_per_wheel=None, sort_order=None, installation_part_type=None, part=None, compatible_keys=None):  # noqa: E501
        """WheelInstallationPart - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._bolt_per_wheel_qty = None
        self._innerpack = None
        self._qty_per_wheel = None
        self._sort_order = None
        self._installation_part_type = None
        self._part = None
        self._compatible_keys = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if bolt_per_wheel_qty is not None:
            self.bolt_per_wheel_qty = bolt_per_wheel_qty
        if innerpack is not None:
            self.innerpack = innerpack
        if qty_per_wheel is not None:
            self.qty_per_wheel = qty_per_wheel
        if sort_order is not None:
            self.sort_order = sort_order
        if installation_part_type is not None:
            self.installation_part_type = installation_part_type
        if part is not None:
            self.part = part
        if compatible_keys is not None:
            self.compatible_keys = compatible_keys

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this WheelInstallationPart.  # noqa: E501

        Thibert part number associated with this part.  # noqa: E501

        :return: The thibert_part_number of this WheelInstallationPart.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this WheelInstallationPart.

        Thibert part number associated with this part.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this WheelInstallationPart.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def bolt_per_wheel_qty(self):
        """Gets the bolt_per_wheel_qty of this WheelInstallationPart.  # noqa: E501

        The numbers of Bolts required per wheel for this vehicle  # noqa: E501

        :return: The bolt_per_wheel_qty of this WheelInstallationPart.  # noqa: E501
        :rtype: str
        """
        return self._bolt_per_wheel_qty

    @bolt_per_wheel_qty.setter
    def bolt_per_wheel_qty(self, bolt_per_wheel_qty):
        """Sets the bolt_per_wheel_qty of this WheelInstallationPart.

        The numbers of Bolts required per wheel for this vehicle  # noqa: E501

        :param bolt_per_wheel_qty: The bolt_per_wheel_qty of this WheelInstallationPart.  # noqa: E501
        :type: str
        """

        self._bolt_per_wheel_qty = bolt_per_wheel_qty

    @property
    def innerpack(self):
        """Gets the innerpack of this WheelInstallationPart.  # noqa: E501

        Qty of item in the pack  # noqa: E501

        :return: The innerpack of this WheelInstallationPart.  # noqa: E501
        :rtype: int
        """
        return self._innerpack

    @innerpack.setter
    def innerpack(self, innerpack):
        """Sets the innerpack of this WheelInstallationPart.

        Qty of item in the pack  # noqa: E501

        :param innerpack: The innerpack of this WheelInstallationPart.  # noqa: E501
        :type: int
        """

        self._innerpack = innerpack

    @property
    def qty_per_wheel(self):
        """Gets the qty_per_wheel of this WheelInstallationPart.  # noqa: E501

        Qty needed per wheel  # noqa: E501

        :return: The qty_per_wheel of this WheelInstallationPart.  # noqa: E501
        :rtype: int
        """
        return self._qty_per_wheel

    @qty_per_wheel.setter
    def qty_per_wheel(self, qty_per_wheel):
        """Sets the qty_per_wheel of this WheelInstallationPart.

        Qty needed per wheel  # noqa: E501

        :param qty_per_wheel: The qty_per_wheel of this WheelInstallationPart.  # noqa: E501
        :type: int
        """

        self._qty_per_wheel = qty_per_wheel

    @property
    def sort_order(self):
        """Gets the sort_order of this WheelInstallationPart.  # noqa: E501


        :return: The sort_order of this WheelInstallationPart.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this WheelInstallationPart.


        :param sort_order: The sort_order of this WheelInstallationPart.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def installation_part_type(self):
        """Gets the installation_part_type of this WheelInstallationPart.  # noqa: E501

        Type of installation part  # noqa: E501

        :return: The installation_part_type of this WheelInstallationPart.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._installation_part_type

    @installation_part_type.setter
    def installation_part_type(self, installation_part_type):
        """Sets the installation_part_type of this WheelInstallationPart.

        Type of installation part  # noqa: E501

        :param installation_part_type: The installation_part_type of this WheelInstallationPart.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._installation_part_type = installation_part_type

    @property
    def part(self):
        """Gets the part of this WheelInstallationPart.  # noqa: E501


        :return: The part of this WheelInstallationPart.  # noqa: E501
        :rtype: Part
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this WheelInstallationPart.


        :param part: The part of this WheelInstallationPart.  # noqa: E501
        :type: Part
        """

        self._part = part

    @property
    def compatible_keys(self):
        """Gets the compatible_keys of this WheelInstallationPart.  # noqa: E501

        List of compatible keys for the installation of a bolt  # noqa: E501

        :return: The compatible_keys of this WheelInstallationPart.  # noqa: E501
        :rtype: list[Part]
        """
        return self._compatible_keys

    @compatible_keys.setter
    def compatible_keys(self, compatible_keys):
        """Sets the compatible_keys of this WheelInstallationPart.

        List of compatible keys for the installation of a bolt  # noqa: E501

        :param compatible_keys: The compatible_keys of this WheelInstallationPart.  # noqa: E501
        :type: list[Part]
        """

        self._compatible_keys = compatible_keys

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
        if issubclass(WheelInstallationPart, dict):
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
        if not isinstance(other, WheelInstallationPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
