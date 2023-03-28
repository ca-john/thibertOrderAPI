# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class FitmentDetails(object):
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
        'is_direct_fit': 'bool',
        'is_direct_fit_image': 'str',
        'is_hub_centric': 'bool',
        'is_hub_centric_image': 'str',
        'is_oem_compatible': 'bool',
        'is_oem_compatible_image': 'str',
        'is_winter_approved': 'bool',
        'is_winter_approved_image': 'str',
        'is_staggered': 'bool',
        'is_staggered_image': 'str',
        'is_valve_included': 'bool'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'is_direct_fit': 'isDirectFit',
        'is_direct_fit_image': 'isDirectFitImage',
        'is_hub_centric': 'isHubCentric',
        'is_hub_centric_image': 'isHubCentricImage',
        'is_oem_compatible': 'isOEMCompatible',
        'is_oem_compatible_image': 'isOEMCompatibleImage',
        'is_winter_approved': 'isWinterApproved',
        'is_winter_approved_image': 'isWinterApprovedImage',
        'is_staggered': 'isStaggered',
        'is_staggered_image': 'isStaggeredImage',
        'is_valve_included': 'isValveIncluded'
    }

    def __init__(self, thibert_part_number=None, is_direct_fit=None, is_direct_fit_image=None, is_hub_centric=None, is_hub_centric_image=None, is_oem_compatible=None, is_oem_compatible_image=None, is_winter_approved=None, is_winter_approved_image=None, is_staggered=None, is_staggered_image=None, is_valve_included=None):  # noqa: E501
        """FitmentDetails - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._is_direct_fit = None
        self._is_direct_fit_image = None
        self._is_hub_centric = None
        self._is_hub_centric_image = None
        self._is_oem_compatible = None
        self._is_oem_compatible_image = None
        self._is_winter_approved = None
        self._is_winter_approved_image = None
        self._is_staggered = None
        self._is_staggered_image = None
        self._is_valve_included = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if is_direct_fit is not None:
            self.is_direct_fit = is_direct_fit
        if is_direct_fit_image is not None:
            self.is_direct_fit_image = is_direct_fit_image
        if is_hub_centric is not None:
            self.is_hub_centric = is_hub_centric
        if is_hub_centric_image is not None:
            self.is_hub_centric_image = is_hub_centric_image
        if is_oem_compatible is not None:
            self.is_oem_compatible = is_oem_compatible
        if is_oem_compatible_image is not None:
            self.is_oem_compatible_image = is_oem_compatible_image
        if is_winter_approved is not None:
            self.is_winter_approved = is_winter_approved
        if is_winter_approved_image is not None:
            self.is_winter_approved_image = is_winter_approved_image
        if is_staggered is not None:
            self.is_staggered = is_staggered
        if is_staggered_image is not None:
            self.is_staggered_image = is_staggered_image
        if is_valve_included is not None:
            self.is_valve_included = is_valve_included

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this FitmentDetails.  # noqa: E501

        Thibert part number associated with this item.  # noqa: E501

        :return: The thibert_part_number of this FitmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this FitmentDetails.

        Thibert part number associated with this item.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this FitmentDetails.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def is_direct_fit(self):
        """Gets the is_direct_fit of this FitmentDetails.  # noqa: E501

        Indicates if the wheel is a direct fit for the vehicle  # noqa: E501

        :return: The is_direct_fit of this FitmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_direct_fit

    @is_direct_fit.setter
    def is_direct_fit(self, is_direct_fit):
        """Sets the is_direct_fit of this FitmentDetails.

        Indicates if the wheel is a direct fit for the vehicle  # noqa: E501

        :param is_direct_fit: The is_direct_fit of this FitmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_direct_fit = is_direct_fit

    @property
    def is_direct_fit_image(self):
        """Gets the is_direct_fit_image of this FitmentDetails.  # noqa: E501

        Icon used to indicates when a wheel is a Direct Fit for the vehicle  # noqa: E501

        :return: The is_direct_fit_image of this FitmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_direct_fit_image

    @is_direct_fit_image.setter
    def is_direct_fit_image(self, is_direct_fit_image):
        """Sets the is_direct_fit_image of this FitmentDetails.

        Icon used to indicates when a wheel is a Direct Fit for the vehicle  # noqa: E501

        :param is_direct_fit_image: The is_direct_fit_image of this FitmentDetails.  # noqa: E501
        :type: str
        """

        self._is_direct_fit_image = is_direct_fit_image

    @property
    def is_hub_centric(self):
        """Gets the is_hub_centric of this FitmentDetails.  # noqa: E501

        Indicates if the wheel is hub centric for the vehicle  # noqa: E501

        :return: The is_hub_centric of this FitmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_hub_centric

    @is_hub_centric.setter
    def is_hub_centric(self, is_hub_centric):
        """Sets the is_hub_centric of this FitmentDetails.

        Indicates if the wheel is hub centric for the vehicle  # noqa: E501

        :param is_hub_centric: The is_hub_centric of this FitmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_hub_centric = is_hub_centric

    @property
    def is_hub_centric_image(self):
        """Gets the is_hub_centric_image of this FitmentDetails.  # noqa: E501

        Icon used to indicates when a wheel is hub centric for the vehicle  # noqa: E501

        :return: The is_hub_centric_image of this FitmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_hub_centric_image

    @is_hub_centric_image.setter
    def is_hub_centric_image(self, is_hub_centric_image):
        """Sets the is_hub_centric_image of this FitmentDetails.

        Icon used to indicates when a wheel is hub centric for the vehicle  # noqa: E501

        :param is_hub_centric_image: The is_hub_centric_image of this FitmentDetails.  # noqa: E501
        :type: str
        """

        self._is_hub_centric_image = is_hub_centric_image

    @property
    def is_oem_compatible(self):
        """Gets the is_oem_compatible of this FitmentDetails.  # noqa: E501

        Indicates if the wheel is OEM compatible for the vehicle  # noqa: E501

        :return: The is_oem_compatible of this FitmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_oem_compatible

    @is_oem_compatible.setter
    def is_oem_compatible(self, is_oem_compatible):
        """Sets the is_oem_compatible of this FitmentDetails.

        Indicates if the wheel is OEM compatible for the vehicle  # noqa: E501

        :param is_oem_compatible: The is_oem_compatible of this FitmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_oem_compatible = is_oem_compatible

    @property
    def is_oem_compatible_image(self):
        """Gets the is_oem_compatible_image of this FitmentDetails.  # noqa: E501

        Icon used to indicates when a wheel is OEM compatible for the vehicle  # noqa: E501

        :return: The is_oem_compatible_image of this FitmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_oem_compatible_image

    @is_oem_compatible_image.setter
    def is_oem_compatible_image(self, is_oem_compatible_image):
        """Sets the is_oem_compatible_image of this FitmentDetails.

        Icon used to indicates when a wheel is OEM compatible for the vehicle  # noqa: E501

        :param is_oem_compatible_image: The is_oem_compatible_image of this FitmentDetails.  # noqa: E501
        :type: str
        """

        self._is_oem_compatible_image = is_oem_compatible_image

    @property
    def is_winter_approved(self):
        """Gets the is_winter_approved of this FitmentDetails.  # noqa: E501

        Indicates if the wheel is winter approuved  # noqa: E501

        :return: The is_winter_approved of this FitmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_winter_approved

    @is_winter_approved.setter
    def is_winter_approved(self, is_winter_approved):
        """Sets the is_winter_approved of this FitmentDetails.

        Indicates if the wheel is winter approuved  # noqa: E501

        :param is_winter_approved: The is_winter_approved of this FitmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_winter_approved = is_winter_approved

    @property
    def is_winter_approved_image(self):
        """Gets the is_winter_approved_image of this FitmentDetails.  # noqa: E501

        Icon used to indicates when a wheel is winter approuved  # noqa: E501

        :return: The is_winter_approved_image of this FitmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_winter_approved_image

    @is_winter_approved_image.setter
    def is_winter_approved_image(self, is_winter_approved_image):
        """Sets the is_winter_approved_image of this FitmentDetails.

        Icon used to indicates when a wheel is winter approuved  # noqa: E501

        :param is_winter_approved_image: The is_winter_approved_image of this FitmentDetails.  # noqa: E501
        :type: str
        """

        self._is_winter_approved_image = is_winter_approved_image

    @property
    def is_staggered(self):
        """Gets the is_staggered of this FitmentDetails.  # noqa: E501

        Indicates if the wheel is staggered for the vehicle  # noqa: E501

        :return: The is_staggered of this FitmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_staggered

    @is_staggered.setter
    def is_staggered(self, is_staggered):
        """Sets the is_staggered of this FitmentDetails.

        Indicates if the wheel is staggered for the vehicle  # noqa: E501

        :param is_staggered: The is_staggered of this FitmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_staggered = is_staggered

    @property
    def is_staggered_image(self):
        """Gets the is_staggered_image of this FitmentDetails.  # noqa: E501

        Icon used to indicates when a wheel is staggered for the vehicle  # noqa: E501

        :return: The is_staggered_image of this FitmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_staggered_image

    @is_staggered_image.setter
    def is_staggered_image(self, is_staggered_image):
        """Sets the is_staggered_image of this FitmentDetails.

        Icon used to indicates when a wheel is staggered for the vehicle  # noqa: E501

        :param is_staggered_image: The is_staggered_image of this FitmentDetails.  # noqa: E501
        :type: str
        """

        self._is_staggered_image = is_staggered_image

    @property
    def is_valve_included(self):
        """Gets the is_valve_included of this FitmentDetails.  # noqa: E501

        Indicates if the valve is included with this wheel  # noqa: E501

        :return: The is_valve_included of this FitmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_valve_included

    @is_valve_included.setter
    def is_valve_included(self, is_valve_included):
        """Sets the is_valve_included of this FitmentDetails.

        Indicates if the valve is included with this wheel  # noqa: E501

        :param is_valve_included: The is_valve_included of this FitmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_valve_included = is_valve_included

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
        if issubclass(FitmentDetails, dict):
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
        if not isinstance(other, FitmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
