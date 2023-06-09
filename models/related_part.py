# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class RelatedPart(object):
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
        'reference_thibert_part_number': 'str',
        'titles': 'list[LocalizedString]',
        'reference_type': 'list[LocalizedString]',
        'images': 'list[Image]'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'reference_thibert_part_number': 'referenceThibertPartNumber',
        'titles': 'titles',
        'reference_type': 'referenceType',
        'images': 'images'
    }

    def __init__(self, thibert_part_number=None, reference_thibert_part_number=None, titles=None, reference_type=None, images=None):  # noqa: E501
        """RelatedPart - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._reference_thibert_part_number = None
        self._titles = None
        self._reference_type = None
        self._images = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if reference_thibert_part_number is not None:
            self.reference_thibert_part_number = reference_thibert_part_number
        if titles is not None:
            self.titles = titles
        if reference_type is not None:
            self.reference_type = reference_type
        if images is not None:
            self.images = images

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this RelatedPart.  # noqa: E501

        Part number of the part  # noqa: E501

        :return: The thibert_part_number of this RelatedPart.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this RelatedPart.

        Part number of the part  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this RelatedPart.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def reference_thibert_part_number(self):
        """Gets the reference_thibert_part_number of this RelatedPart.  # noqa: E501

        Part number of the related part  # noqa: E501

        :return: The reference_thibert_part_number of this RelatedPart.  # noqa: E501
        :rtype: str
        """
        return self._reference_thibert_part_number

    @reference_thibert_part_number.setter
    def reference_thibert_part_number(self, reference_thibert_part_number):
        """Sets the reference_thibert_part_number of this RelatedPart.

        Part number of the related part  # noqa: E501

        :param reference_thibert_part_number: The reference_thibert_part_number of this RelatedPart.  # noqa: E501
        :type: str
        """

        self._reference_thibert_part_number = reference_thibert_part_number

    @property
    def titles(self):
        """Gets the titles of this RelatedPart.  # noqa: E501

        Titles of the related part.  # noqa: E501

        :return: The titles of this RelatedPart.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this RelatedPart.

        Titles of the related part.  # noqa: E501

        :param titles: The titles of this RelatedPart.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._titles = titles

    @property
    def reference_type(self):
        """Gets the reference_type of this RelatedPart.  # noqa: E501

        Short description of this item.  # noqa: E501

        :return: The reference_type of this RelatedPart.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this RelatedPart.

        Short description of this item.  # noqa: E501

        :param reference_type: The reference_type of this RelatedPart.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._reference_type = reference_type

    @property
    def images(self):
        """Gets the images of this RelatedPart.  # noqa: E501

        List of all images associated with this related part.  # noqa: E501

        :return: The images of this RelatedPart.  # noqa: E501
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this RelatedPart.

        List of all images associated with this related part.  # noqa: E501

        :param images: The images of this RelatedPart.  # noqa: E501
        :type: list[Image]
        """

        self._images = images

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
        if issubclass(RelatedPart, dict):
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
        if not isinstance(other, RelatedPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
