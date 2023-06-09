# coding: utf-8

"""
API Spec for Thibert
"""

import pprint
import re  # noqa: F401

import six

class TaskCreationRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'assigned_group': 'str',
        'title': 'str',
        'description': 'str',
        'items': 'list[TaskItem]'
    }

    attribute_map = {
        'assigned_group': 'assignedGroup',
        'title': 'title',
        'description': 'description',
        'items': 'items'
    }

    def __init__(self, assigned_group=None, title=None, description=None, items=None):  # noqa: E501
        """TaskCreationRequest - a model defined in Swagger"""  # noqa: E501
        self._assigned_group = None
        self._title = None
        self._description = None
        self._items = None
        self.discriminator = None
        if assigned_group is not None:
            self.assigned_group = assigned_group
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if items is not None:
            self.items = items

    @property
    def assigned_group(self):
        """Gets the assigned_group of this TaskCreationRequest.  # noqa: E501


        :return: The assigned_group of this TaskCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._assigned_group

    @assigned_group.setter
    def assigned_group(self, assigned_group):
        """Sets the assigned_group of this TaskCreationRequest.


        :param assigned_group: The assigned_group of this TaskCreationRequest.  # noqa: E501
        :type: str
        """

        self._assigned_group = assigned_group

    @property
    def title(self):
        """Gets the title of this TaskCreationRequest.  # noqa: E501


        :return: The title of this TaskCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskCreationRequest.


        :param title: The title of this TaskCreationRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this TaskCreationRequest.  # noqa: E501


        :return: The description of this TaskCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskCreationRequest.


        :param description: The description of this TaskCreationRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def items(self):
        """Gets the items of this TaskCreationRequest.  # noqa: E501


        :return: The items of this TaskCreationRequest.  # noqa: E501
        :rtype: list[TaskItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TaskCreationRequest.


        :param items: The items of this TaskCreationRequest.  # noqa: E501
        :type: list[TaskItem]
        """

        self._items = items

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
        if issubclass(TaskCreationRequest, dict):
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
        if not isinstance(other, TaskCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
