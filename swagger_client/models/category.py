# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class Category(object):
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
        'category_id': 'str',
        'category_level': 'int',
        'category_id_level1': 'str',
        'category_name_level1': 'list[LocalizedString]',
        'category_id_level2': 'str',
        'category_name_level2': 'list[LocalizedString]',
        'category_id_level3': 'str',
        'category_name_level3': 'list[LocalizedString]',
        'category_id_level4': 'str',
        'category_name_level4': 'list[LocalizedString]',
        'category_id_level5': 'str',
        'category_name_level5': 'list[LocalizedString]',
        'category_id_level6': 'str',
        'category_name_level6': 'list[LocalizedString]',
        'category_id_level7': 'str',
        'category_name_level7': 'list[LocalizedString]',
        'category_image_url': 'str'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'category_id': 'categoryId',
        'category_level': 'categoryLevel',
        'category_id_level1': 'categoryIdLevel1',
        'category_name_level1': 'categoryNameLevel1',
        'category_id_level2': 'categoryIdLevel2',
        'category_name_level2': 'categoryNameLevel2',
        'category_id_level3': 'categoryIdLevel3',
        'category_name_level3': 'categoryNameLevel3',
        'category_id_level4': 'categoryIdLevel4',
        'category_name_level4': 'categoryNameLevel4',
        'category_id_level5': 'categoryIdLevel5',
        'category_name_level5': 'categoryNameLevel5',
        'category_id_level6': 'categoryIdLevel6',
        'category_name_level6': 'categoryNameLevel6',
        'category_id_level7': 'categoryIdLevel7',
        'category_name_level7': 'categoryNameLevel7',
        'category_image_url': 'categoryImageURL'
    }

    def __init__(self, thibert_part_number=None, category_id=None, category_level=None, category_id_level1=None, category_name_level1=None, category_id_level2=None, category_name_level2=None, category_id_level3=None, category_name_level3=None, category_id_level4=None, category_name_level4=None, category_id_level5=None, category_name_level5=None, category_id_level6=None, category_name_level6=None, category_id_level7=None, category_name_level7=None, category_image_url=None):  # noqa: E501
        """Category - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._category_id = None
        self._category_level = None
        self._category_id_level1 = None
        self._category_name_level1 = None
        self._category_id_level2 = None
        self._category_name_level2 = None
        self._category_id_level3 = None
        self._category_name_level3 = None
        self._category_id_level4 = None
        self._category_name_level4 = None
        self._category_id_level5 = None
        self._category_name_level5 = None
        self._category_id_level6 = None
        self._category_name_level6 = None
        self._category_id_level7 = None
        self._category_name_level7 = None
        self._category_image_url = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if category_id is not None:
            self.category_id = category_id
        if category_level is not None:
            self.category_level = category_level
        if category_id_level1 is not None:
            self.category_id_level1 = category_id_level1
        if category_name_level1 is not None:
            self.category_name_level1 = category_name_level1
        if category_id_level2 is not None:
            self.category_id_level2 = category_id_level2
        if category_name_level2 is not None:
            self.category_name_level2 = category_name_level2
        if category_id_level3 is not None:
            self.category_id_level3 = category_id_level3
        if category_name_level3 is not None:
            self.category_name_level3 = category_name_level3
        if category_id_level4 is not None:
            self.category_id_level4 = category_id_level4
        if category_name_level4 is not None:
            self.category_name_level4 = category_name_level4
        if category_id_level5 is not None:
            self.category_id_level5 = category_id_level5
        if category_name_level5 is not None:
            self.category_name_level5 = category_name_level5
        if category_id_level6 is not None:
            self.category_id_level6 = category_id_level6
        if category_name_level6 is not None:
            self.category_name_level6 = category_name_level6
        if category_id_level7 is not None:
            self.category_id_level7 = category_id_level7
        if category_name_level7 is not None:
            self.category_name_level7 = category_name_level7
        if category_image_url is not None:
            self.category_image_url = category_image_url

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this Category.  # noqa: E501

        Part number of the item associated with this category.  # noqa: E501

        :return: The thibert_part_number of this Category.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this Category.

        Part number of the item associated with this category.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this Category.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def category_id(self):
        """Gets the category_id of this Category.  # noqa: E501

        CategoryID of the category represented in this hierarchy  # noqa: E501

        :return: The category_id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Category.

        CategoryID of the category represented in this hierarchy  # noqa: E501

        :param category_id: The category_id of this Category.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_level(self):
        """Gets the category_level of this Category.  # noqa: E501

        Level of the category represented in this hierarchy  # noqa: E501

        :return: The category_level of this Category.  # noqa: E501
        :rtype: int
        """
        return self._category_level

    @category_level.setter
    def category_level(self, category_level):
        """Sets the category_level of this Category.

        Level of the category represented in this hierarchy  # noqa: E501

        :param category_level: The category_level of this Category.  # noqa: E501
        :type: int
        """

        self._category_level = category_level

    @property
    def category_id_level1(self):
        """Gets the category_id_level1 of this Category.  # noqa: E501

        CategoryID for the Level1 of this hierarchy  # noqa: E501

        :return: The category_id_level1 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level1

    @category_id_level1.setter
    def category_id_level1(self, category_id_level1):
        """Sets the category_id_level1 of this Category.

        CategoryID for the Level1 of this hierarchy  # noqa: E501

        :param category_id_level1: The category_id_level1 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level1 = category_id_level1

    @property
    def category_name_level1(self):
        """Gets the category_name_level1 of this Category.  # noqa: E501

        Name of the category at Level1  # noqa: E501

        :return: The category_name_level1 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level1

    @category_name_level1.setter
    def category_name_level1(self, category_name_level1):
        """Sets the category_name_level1 of this Category.

        Name of the category at Level1  # noqa: E501

        :param category_name_level1: The category_name_level1 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level1 = category_name_level1

    @property
    def category_id_level2(self):
        """Gets the category_id_level2 of this Category.  # noqa: E501

        CategoryID for the Level2 of this hierarchy  # noqa: E501

        :return: The category_id_level2 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level2

    @category_id_level2.setter
    def category_id_level2(self, category_id_level2):
        """Sets the category_id_level2 of this Category.

        CategoryID for the Level2 of this hierarchy  # noqa: E501

        :param category_id_level2: The category_id_level2 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level2 = category_id_level2

    @property
    def category_name_level2(self):
        """Gets the category_name_level2 of this Category.  # noqa: E501

        Name of the category at Level2  # noqa: E501

        :return: The category_name_level2 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level2

    @category_name_level2.setter
    def category_name_level2(self, category_name_level2):
        """Sets the category_name_level2 of this Category.

        Name of the category at Level2  # noqa: E501

        :param category_name_level2: The category_name_level2 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level2 = category_name_level2

    @property
    def category_id_level3(self):
        """Gets the category_id_level3 of this Category.  # noqa: E501

        CategoryID for the Level3 of this hierarchy  # noqa: E501

        :return: The category_id_level3 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level3

    @category_id_level3.setter
    def category_id_level3(self, category_id_level3):
        """Sets the category_id_level3 of this Category.

        CategoryID for the Level3 of this hierarchy  # noqa: E501

        :param category_id_level3: The category_id_level3 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level3 = category_id_level3

    @property
    def category_name_level3(self):
        """Gets the category_name_level3 of this Category.  # noqa: E501

        Name of the category at Level3  # noqa: E501

        :return: The category_name_level3 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level3

    @category_name_level3.setter
    def category_name_level3(self, category_name_level3):
        """Sets the category_name_level3 of this Category.

        Name of the category at Level3  # noqa: E501

        :param category_name_level3: The category_name_level3 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level3 = category_name_level3

    @property
    def category_id_level4(self):
        """Gets the category_id_level4 of this Category.  # noqa: E501

        CategoryID for the Level4 of this hierarchy  # noqa: E501

        :return: The category_id_level4 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level4

    @category_id_level4.setter
    def category_id_level4(self, category_id_level4):
        """Sets the category_id_level4 of this Category.

        CategoryID for the Level4 of this hierarchy  # noqa: E501

        :param category_id_level4: The category_id_level4 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level4 = category_id_level4

    @property
    def category_name_level4(self):
        """Gets the category_name_level4 of this Category.  # noqa: E501

        Name of the category at Level4  # noqa: E501

        :return: The category_name_level4 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level4

    @category_name_level4.setter
    def category_name_level4(self, category_name_level4):
        """Sets the category_name_level4 of this Category.

        Name of the category at Level4  # noqa: E501

        :param category_name_level4: The category_name_level4 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level4 = category_name_level4

    @property
    def category_id_level5(self):
        """Gets the category_id_level5 of this Category.  # noqa: E501

        CategoryID for the Level5 of this hierarchy  # noqa: E501

        :return: The category_id_level5 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level5

    @category_id_level5.setter
    def category_id_level5(self, category_id_level5):
        """Sets the category_id_level5 of this Category.

        CategoryID for the Level5 of this hierarchy  # noqa: E501

        :param category_id_level5: The category_id_level5 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level5 = category_id_level5

    @property
    def category_name_level5(self):
        """Gets the category_name_level5 of this Category.  # noqa: E501

        Name of the category at Level5  # noqa: E501

        :return: The category_name_level5 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level5

    @category_name_level5.setter
    def category_name_level5(self, category_name_level5):
        """Sets the category_name_level5 of this Category.

        Name of the category at Level5  # noqa: E501

        :param category_name_level5: The category_name_level5 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level5 = category_name_level5

    @property
    def category_id_level6(self):
        """Gets the category_id_level6 of this Category.  # noqa: E501

        CategoryID for the Level6 of this hierarchy  # noqa: E501

        :return: The category_id_level6 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level6

    @category_id_level6.setter
    def category_id_level6(self, category_id_level6):
        """Sets the category_id_level6 of this Category.

        CategoryID for the Level6 of this hierarchy  # noqa: E501

        :param category_id_level6: The category_id_level6 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level6 = category_id_level6

    @property
    def category_name_level6(self):
        """Gets the category_name_level6 of this Category.  # noqa: E501

        Name of the category at Level6  # noqa: E501

        :return: The category_name_level6 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level6

    @category_name_level6.setter
    def category_name_level6(self, category_name_level6):
        """Sets the category_name_level6 of this Category.

        Name of the category at Level6  # noqa: E501

        :param category_name_level6: The category_name_level6 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level6 = category_name_level6

    @property
    def category_id_level7(self):
        """Gets the category_id_level7 of this Category.  # noqa: E501

        CategoryID for the Level7 of this hierarchy  # noqa: E501

        :return: The category_id_level7 of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_id_level7

    @category_id_level7.setter
    def category_id_level7(self, category_id_level7):
        """Sets the category_id_level7 of this Category.

        CategoryID for the Level7 of this hierarchy  # noqa: E501

        :param category_id_level7: The category_id_level7 of this Category.  # noqa: E501
        :type: str
        """

        self._category_id_level7 = category_id_level7

    @property
    def category_name_level7(self):
        """Gets the category_name_level7 of this Category.  # noqa: E501

        Name of the category at Level7  # noqa: E501

        :return: The category_name_level7 of this Category.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._category_name_level7

    @category_name_level7.setter
    def category_name_level7(self, category_name_level7):
        """Sets the category_name_level7 of this Category.

        Name of the category at Level7  # noqa: E501

        :param category_name_level7: The category_name_level7 of this Category.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._category_name_level7 = category_name_level7

    @property
    def category_image_url(self):
        """Gets the category_image_url of this Category.  # noqa: E501

        Image of the category represented in this hierarchy  # noqa: E501

        :return: The category_image_url of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_image_url

    @category_image_url.setter
    def category_image_url(self, category_image_url):
        """Sets the category_image_url of this Category.

        Image of the category represented in this hierarchy  # noqa: E501

        :param category_image_url: The category_image_url of this Category.  # noqa: E501
        :type: str
        """

        self._category_image_url = category_image_url

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
        if issubclass(Category, dict):
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
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
