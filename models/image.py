# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class Image(object):
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
        'image_url': 'str',
        'image_type': 'str'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'image_url': 'imageURL',
        'image_type': 'imageType'
    }

    def __init__(self, thibert_part_number=None, image_url=None, image_type=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._image_url = None
        self._image_type = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if image_url is not None:
            self.image_url = image_url
        if image_type is not None:
            self.image_type = image_type

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this Image.  # noqa: E501

        Part number of the item associated with this image.  # noqa: E501

        :return: The thibert_part_number of this Image.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this Image.

        Part number of the item associated with this image.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this Image.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def image_url(self):
        """Gets the image_url of this Image.  # noqa: E501

        URL of where the image is hosted and can be retrived.  # noqa: E501

        :return: The image_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Image.

        URL of where the image is hosted and can be retrived.  # noqa: E501

        :param image_url: The image_url of this Image.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def image_type(self):
        """Gets the image_type of this Image.  # noqa: E501

        Type of the image.  # noqa: E501

        :return: The image_type of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this Image.

        Type of the image.  # noqa: E501

        :param image_type: The image_type of this Image.  # noqa: E501
        :type: str
        """

        self._image_type = image_type

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
