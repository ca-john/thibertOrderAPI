# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class Part(object):
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
        'your_price': 'float',
        'your_price_currency_code': 'str',
        'jobber_price': 'list[PricesByCurrencies]',
        'msrp_price': 'list[PricesByCurrencies]',
        'map_price': 'list[PricesByCurrencies]',
        'vendor_part_number': 'str',
        'brand': 'str',
        'model': 'str',
        'series': 'str',
        'web_status': 'str',
        'titles': 'list[LocalizedString]',
        'short_descriptions': 'list[LocalizedString]',
        'long_descriptions': 'list[LocalizedString]',
        'application_notes': 'list[LocalizedString]',
        'replacement_item': 'str',
        'wheel_part_type_id': 'str',
        'wheel_part_type': 'list[LocalizedString]',
        'is_on_clearance': 'bool',
        'is_on_clearance_title': 'list[LocalizedString]',
        'is_new_arrival': 'bool',
        'is_new_arrival_title': 'list[LocalizedString]',
        'is_overweight': 'bool',
        'is_oversize': 'bool',
        'unit_net_weight_packed_lbs': 'float',
        'unit_height_packed': 'float',
        'unit_length_packed': 'float',
        'unit_width_packed': 'float',
        'unit_upc_code': 'str',
        'last_modification_date': 'datetime',
        'images': 'list[Image]',
        'attributes': 'list[Attribute]',
        'inventories': 'list[Inventory]',
        'categories': 'list[Category]',
        'fitment_details': 'FitmentDetails',
        'related_parts': 'list[RelatedPart]'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'your_price': 'yourPrice',
        'your_price_currency_code': 'yourPriceCurrencyCode',
        'jobber_price': 'jobberPrice',
        'msrp_price': 'msrpPrice',
        'map_price': 'mapPrice',
        'vendor_part_number': 'vendorPartNumber',
        'brand': 'brand',
        'model': 'model',
        'series': 'series',
        'web_status': 'webStatus',
        'titles': 'titles',
        'short_descriptions': 'shortDescriptions',
        'long_descriptions': 'longDescriptions',
        'application_notes': 'applicationNotes',
        'replacement_item': 'replacementItem',
        'wheel_part_type_id': 'wheelPartTypeID',
        'wheel_part_type': 'wheelPartType',
        'is_on_clearance': 'isOnClearance',
        'is_on_clearance_title': 'isOnClearanceTitle',
        'is_new_arrival': 'isNewArrival',
        'is_new_arrival_title': 'isNewArrivalTitle',
        'is_overweight': 'isOverweight',
        'is_oversize': 'isOversize',
        'unit_net_weight_packed_lbs': 'unitNetWeightPackedLBS',
        'unit_height_packed': 'unitHeightPacked',
        'unit_length_packed': 'unitLengthPacked',
        'unit_width_packed': 'unitWidthPacked',
        'unit_upc_code': 'unitUPCCode',
        'last_modification_date': 'lastModificationDate',
        'images': 'images',
        'attributes': 'attributes',
        'inventories': 'inventories',
        'categories': 'categories',
        'fitment_details': 'fitmentDetails',
        'related_parts': 'relatedParts'
    }

    def __init__(self, thibert_part_number=None, your_price=None, your_price_currency_code=None, jobber_price=None, msrp_price=None, map_price=None, vendor_part_number=None, brand=None, model=None, series=None, web_status=None, titles=None, short_descriptions=None, long_descriptions=None, application_notes=None, replacement_item=None, wheel_part_type_id=None, wheel_part_type=None, is_on_clearance=None, is_on_clearance_title=None, is_new_arrival=None, is_new_arrival_title=None, is_overweight=None, is_oversize=None, unit_net_weight_packed_lbs=None, unit_height_packed=None, unit_length_packed=None, unit_width_packed=None, unit_upc_code=None, last_modification_date=None, images=None, attributes=None, inventories=None, categories=None, fitment_details=None, related_parts=None):  # noqa: E501
        """Part - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._your_price = None
        self._your_price_currency_code = None
        self._jobber_price = None
        self._msrp_price = None
        self._map_price = None
        self._vendor_part_number = None
        self._brand = None
        self._model = None
        self._series = None
        self._web_status = None
        self._titles = None
        self._short_descriptions = None
        self._long_descriptions = None
        self._application_notes = None
        self._replacement_item = None
        self._wheel_part_type_id = None
        self._wheel_part_type = None
        self._is_on_clearance = None
        self._is_on_clearance_title = None
        self._is_new_arrival = None
        self._is_new_arrival_title = None
        self._is_overweight = None
        self._is_oversize = None
        self._unit_net_weight_packed_lbs = None
        self._unit_height_packed = None
        self._unit_length_packed = None
        self._unit_width_packed = None
        self._unit_upc_code = None
        self._last_modification_date = None
        self._images = None
        self._attributes = None
        self._inventories = None
        self._categories = None
        self._fitment_details = None
        self._related_parts = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if your_price is not None:
            self.your_price = your_price
        if your_price_currency_code is not None:
            self.your_price_currency_code = your_price_currency_code
        if jobber_price is not None:
            self.jobber_price = jobber_price
        if msrp_price is not None:
            self.msrp_price = msrp_price
        if map_price is not None:
            self.map_price = map_price
        if vendor_part_number is not None:
            self.vendor_part_number = vendor_part_number
        if brand is not None:
            self.brand = brand
        if model is not None:
            self.model = model
        if series is not None:
            self.series = series
        if web_status is not None:
            self.web_status = web_status
        if titles is not None:
            self.titles = titles
        if short_descriptions is not None:
            self.short_descriptions = short_descriptions
        if long_descriptions is not None:
            self.long_descriptions = long_descriptions
        if application_notes is not None:
            self.application_notes = application_notes
        if replacement_item is not None:
            self.replacement_item = replacement_item
        if wheel_part_type_id is not None:
            self.wheel_part_type_id = wheel_part_type_id
        if wheel_part_type is not None:
            self.wheel_part_type = wheel_part_type
        if is_on_clearance is not None:
            self.is_on_clearance = is_on_clearance
        if is_on_clearance_title is not None:
            self.is_on_clearance_title = is_on_clearance_title
        if is_new_arrival is not None:
            self.is_new_arrival = is_new_arrival
        if is_new_arrival_title is not None:
            self.is_new_arrival_title = is_new_arrival_title
        if is_overweight is not None:
            self.is_overweight = is_overweight
        if is_oversize is not None:
            self.is_oversize = is_oversize
        if unit_net_weight_packed_lbs is not None:
            self.unit_net_weight_packed_lbs = unit_net_weight_packed_lbs
        if unit_height_packed is not None:
            self.unit_height_packed = unit_height_packed
        if unit_length_packed is not None:
            self.unit_length_packed = unit_length_packed
        if unit_width_packed is not None:
            self.unit_width_packed = unit_width_packed
        if unit_upc_code is not None:
            self.unit_upc_code = unit_upc_code
        if last_modification_date is not None:
            self.last_modification_date = last_modification_date
        if images is not None:
            self.images = images
        if attributes is not None:
            self.attributes = attributes
        if inventories is not None:
            self.inventories = inventories
        if categories is not None:
            self.categories = categories
        if fitment_details is not None:
            self.fitment_details = fitment_details
        if related_parts is not None:
            self.related_parts = related_parts

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this Part.  # noqa: E501

        Thibert part number associated with this item.  # noqa: E501

        :return: The thibert_part_number of this Part.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this Part.

        Thibert part number associated with this item.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this Part.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def your_price(self):
        """Gets the your_price of this Part.  # noqa: E501

        Price of this item for the given customer.  # noqa: E501

        :return: The your_price of this Part.  # noqa: E501
        :rtype: float
        """
        return self._your_price

    @your_price.setter
    def your_price(self, your_price):
        """Sets the your_price of this Part.

        Price of this item for the given customer.  # noqa: E501

        :param your_price: The your_price of this Part.  # noqa: E501
        :type: float
        """

        self._your_price = your_price

    @property
    def your_price_currency_code(self):
        """Gets the your_price_currency_code of this Part.  # noqa: E501

        Currency of YourPrice for the given customer.  # noqa: E501

        :return: The your_price_currency_code of this Part.  # noqa: E501
        :rtype: str
        """
        return self._your_price_currency_code

    @your_price_currency_code.setter
    def your_price_currency_code(self, your_price_currency_code):
        """Sets the your_price_currency_code of this Part.

        Currency of YourPrice for the given customer.  # noqa: E501

        :param your_price_currency_code: The your_price_currency_code of this Part.  # noqa: E501
        :type: str
        """

        self._your_price_currency_code = your_price_currency_code

    @property
    def jobber_price(self):
        """Gets the jobber_price of this Part.  # noqa: E501

        Jobber price of this item.  # noqa: E501

        :return: The jobber_price of this Part.  # noqa: E501
        :rtype: list[PricesByCurrencies]
        """
        return self._jobber_price

    @jobber_price.setter
    def jobber_price(self, jobber_price):
        """Sets the jobber_price of this Part.

        Jobber price of this item.  # noqa: E501

        :param jobber_price: The jobber_price of this Part.  # noqa: E501
        :type: list[PricesByCurrencies]
        """

        self._jobber_price = jobber_price

    @property
    def msrp_price(self):
        """Gets the msrp_price of this Part.  # noqa: E501

        Manufacturer's suggested retail price of this item.  # noqa: E501

        :return: The msrp_price of this Part.  # noqa: E501
        :rtype: list[PricesByCurrencies]
        """
        return self._msrp_price

    @msrp_price.setter
    def msrp_price(self, msrp_price):
        """Sets the msrp_price of this Part.

        Manufacturer's suggested retail price of this item.  # noqa: E501

        :param msrp_price: The msrp_price of this Part.  # noqa: E501
        :type: list[PricesByCurrencies]
        """

        self._msrp_price = msrp_price

    @property
    def map_price(self):
        """Gets the map_price of this Part.  # noqa: E501

        Manufacturer's suggested retail price of this item.  # noqa: E501

        :return: The map_price of this Part.  # noqa: E501
        :rtype: list[PricesByCurrencies]
        """
        return self._map_price

    @map_price.setter
    def map_price(self, map_price):
        """Sets the map_price of this Part.

        Manufacturer's suggested retail price of this item.  # noqa: E501

        :param map_price: The map_price of this Part.  # noqa: E501
        :type: list[PricesByCurrencies]
        """

        self._map_price = map_price

    @property
    def vendor_part_number(self):
        """Gets the vendor_part_number of this Part.  # noqa: E501

        Manufacturer's part number of this item.  # noqa: E501

        :return: The vendor_part_number of this Part.  # noqa: E501
        :rtype: str
        """
        return self._vendor_part_number

    @vendor_part_number.setter
    def vendor_part_number(self, vendor_part_number):
        """Sets the vendor_part_number of this Part.

        Manufacturer's part number of this item.  # noqa: E501

        :param vendor_part_number: The vendor_part_number of this Part.  # noqa: E501
        :type: str
        """

        self._vendor_part_number = vendor_part_number

    @property
    def brand(self):
        """Gets the brand of this Part.  # noqa: E501

        Brand associated with this item.  # noqa: E501

        :return: The brand of this Part.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Part.

        Brand associated with this item.  # noqa: E501

        :param brand: The brand of this Part.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def model(self):
        """Gets the model of this Part.  # noqa: E501

        Model of this item.  # noqa: E501

        :return: The model of this Part.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Part.

        Model of this item.  # noqa: E501

        :param model: The model of this Part.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def series(self):
        """Gets the series of this Part.  # noqa: E501

        Series of this item.  # noqa: E501

        :return: The series of this Part.  # noqa: E501
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this Part.

        Series of this item.  # noqa: E501

        :param series: The series of this Part.  # noqa: E501
        :type: str
        """

        self._series = series

    @property
    def web_status(self):
        """Gets the web_status of this Part.  # noqa: E501

        Availability status of this item.  # noqa: E501

        :return: The web_status of this Part.  # noqa: E501
        :rtype: str
        """
        return self._web_status

    @web_status.setter
    def web_status(self, web_status):
        """Sets the web_status of this Part.

        Availability status of this item.  # noqa: E501

        :param web_status: The web_status of this Part.  # noqa: E501
        :type: str
        """

        self._web_status = web_status

    @property
    def titles(self):
        """Gets the titles of this Part.  # noqa: E501

        Titles of this item.  # noqa: E501

        :return: The titles of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this Part.

        Titles of this item.  # noqa: E501

        :param titles: The titles of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._titles = titles

    @property
    def short_descriptions(self):
        """Gets the short_descriptions of this Part.  # noqa: E501

        Short description of this item.  # noqa: E501

        :return: The short_descriptions of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._short_descriptions

    @short_descriptions.setter
    def short_descriptions(self, short_descriptions):
        """Sets the short_descriptions of this Part.

        Short description of this item.  # noqa: E501

        :param short_descriptions: The short_descriptions of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._short_descriptions = short_descriptions

    @property
    def long_descriptions(self):
        """Gets the long_descriptions of this Part.  # noqa: E501

        Long description of this item.  # noqa: E501

        :return: The long_descriptions of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._long_descriptions

    @long_descriptions.setter
    def long_descriptions(self, long_descriptions):
        """Sets the long_descriptions of this Part.

        Long description of this item.  # noqa: E501

        :param long_descriptions: The long_descriptions of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._long_descriptions = long_descriptions

    @property
    def application_notes(self):
        """Gets the application_notes of this Part.  # noqa: E501

        Application note for the buyer.  # noqa: E501

        :return: The application_notes of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._application_notes

    @application_notes.setter
    def application_notes(self, application_notes):
        """Sets the application_notes of this Part.

        Application note for the buyer.  # noqa: E501

        :param application_notes: The application_notes of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._application_notes = application_notes

    @property
    def replacement_item(self):
        """Gets the replacement_item of this Part.  # noqa: E501

        Item which replaces this item.  # noqa: E501

        :return: The replacement_item of this Part.  # noqa: E501
        :rtype: str
        """
        return self._replacement_item

    @replacement_item.setter
    def replacement_item(self, replacement_item):
        """Sets the replacement_item of this Part.

        Item which replaces this item.  # noqa: E501

        :param replacement_item: The replacement_item of this Part.  # noqa: E501
        :type: str
        """

        self._replacement_item = replacement_item

    @property
    def wheel_part_type_id(self):
        """Gets the wheel_part_type_id of this Part.  # noqa: E501

        WheelPartTypeID (00030 = Dually, 00076 = Styled Steel, 00021 = Steel, 00020 = Alloy)  # noqa: E501

        :return: The wheel_part_type_id of this Part.  # noqa: E501
        :rtype: str
        """
        return self._wheel_part_type_id

    @wheel_part_type_id.setter
    def wheel_part_type_id(self, wheel_part_type_id):
        """Sets the wheel_part_type_id of this Part.

        WheelPartTypeID (00030 = Dually, 00076 = Styled Steel, 00021 = Steel, 00020 = Alloy)  # noqa: E501

        :param wheel_part_type_id: The wheel_part_type_id of this Part.  # noqa: E501
        :type: str
        """

        self._wheel_part_type_id = wheel_part_type_id

    @property
    def wheel_part_type(self):
        """Gets the wheel_part_type of this Part.  # noqa: E501

        Wheel Part Type (Dually, Styled Steel, Steel, Alloy) in english and french  # noqa: E501

        :return: The wheel_part_type of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._wheel_part_type

    @wheel_part_type.setter
    def wheel_part_type(self, wheel_part_type):
        """Sets the wheel_part_type of this Part.

        Wheel Part Type (Dually, Styled Steel, Steel, Alloy) in english and french  # noqa: E501

        :param wheel_part_type: The wheel_part_type of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._wheel_part_type = wheel_part_type

    @property
    def is_on_clearance(self):
        """Gets the is_on_clearance of this Part.  # noqa: E501

        Indicates if this part is on clearance  # noqa: E501

        :return: The is_on_clearance of this Part.  # noqa: E501
        :rtype: bool
        """
        return self._is_on_clearance

    @is_on_clearance.setter
    def is_on_clearance(self, is_on_clearance):
        """Sets the is_on_clearance of this Part.

        Indicates if this part is on clearance  # noqa: E501

        :param is_on_clearance: The is_on_clearance of this Part.  # noqa: E501
        :type: bool
        """

        self._is_on_clearance = is_on_clearance

    @property
    def is_on_clearance_title(self):
        """Gets the is_on_clearance_title of this Part.  # noqa: E501

        Title of the Clearance  # noqa: E501

        :return: The is_on_clearance_title of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._is_on_clearance_title

    @is_on_clearance_title.setter
    def is_on_clearance_title(self, is_on_clearance_title):
        """Sets the is_on_clearance_title of this Part.

        Title of the Clearance  # noqa: E501

        :param is_on_clearance_title: The is_on_clearance_title of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._is_on_clearance_title = is_on_clearance_title

    @property
    def is_new_arrival(self):
        """Gets the is_new_arrival of this Part.  # noqa: E501

        Indicates if this part is a new arrival  # noqa: E501

        :return: The is_new_arrival of this Part.  # noqa: E501
        :rtype: bool
        """
        return self._is_new_arrival

    @is_new_arrival.setter
    def is_new_arrival(self, is_new_arrival):
        """Sets the is_new_arrival of this Part.

        Indicates if this part is a new arrival  # noqa: E501

        :param is_new_arrival: The is_new_arrival of this Part.  # noqa: E501
        :type: bool
        """

        self._is_new_arrival = is_new_arrival

    @property
    def is_new_arrival_title(self):
        """Gets the is_new_arrival_title of this Part.  # noqa: E501

        Title of the new arrival  # noqa: E501

        :return: The is_new_arrival_title of this Part.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._is_new_arrival_title

    @is_new_arrival_title.setter
    def is_new_arrival_title(self, is_new_arrival_title):
        """Sets the is_new_arrival_title of this Part.

        Title of the new arrival  # noqa: E501

        :param is_new_arrival_title: The is_new_arrival_title of this Part.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._is_new_arrival_title = is_new_arrival_title

    @property
    def is_overweight(self):
        """Gets the is_overweight of this Part.  # noqa: E501

        Indicates if this part is Overweight  # noqa: E501

        :return: The is_overweight of this Part.  # noqa: E501
        :rtype: bool
        """
        return self._is_overweight

    @is_overweight.setter
    def is_overweight(self, is_overweight):
        """Sets the is_overweight of this Part.

        Indicates if this part is Overweight  # noqa: E501

        :param is_overweight: The is_overweight of this Part.  # noqa: E501
        :type: bool
        """

        self._is_overweight = is_overweight

    @property
    def is_oversize(self):
        """Gets the is_oversize of this Part.  # noqa: E501

        Indicates if this part is Oversize  # noqa: E501

        :return: The is_oversize of this Part.  # noqa: E501
        :rtype: bool
        """
        return self._is_oversize

    @is_oversize.setter
    def is_oversize(self, is_oversize):
        """Sets the is_oversize of this Part.

        Indicates if this part is Oversize  # noqa: E501

        :param is_oversize: The is_oversize of this Part.  # noqa: E501
        :type: bool
        """

        self._is_oversize = is_oversize

    @property
    def unit_net_weight_packed_lbs(self):
        """Gets the unit_net_weight_packed_lbs of this Part.  # noqa: E501

        Indicate the unit weight packed (lbs)  # noqa: E501

        :return: The unit_net_weight_packed_lbs of this Part.  # noqa: E501
        :rtype: float
        """
        return self._unit_net_weight_packed_lbs

    @unit_net_weight_packed_lbs.setter
    def unit_net_weight_packed_lbs(self, unit_net_weight_packed_lbs):
        """Sets the unit_net_weight_packed_lbs of this Part.

        Indicate the unit weight packed (lbs)  # noqa: E501

        :param unit_net_weight_packed_lbs: The unit_net_weight_packed_lbs of this Part.  # noqa: E501
        :type: float
        """

        self._unit_net_weight_packed_lbs = unit_net_weight_packed_lbs

    @property
    def unit_height_packed(self):
        """Gets the unit_height_packed of this Part.  # noqa: E501

        Indicate the Height packed (inch)  # noqa: E501

        :return: The unit_height_packed of this Part.  # noqa: E501
        :rtype: float
        """
        return self._unit_height_packed

    @unit_height_packed.setter
    def unit_height_packed(self, unit_height_packed):
        """Sets the unit_height_packed of this Part.

        Indicate the Height packed (inch)  # noqa: E501

        :param unit_height_packed: The unit_height_packed of this Part.  # noqa: E501
        :type: float
        """

        self._unit_height_packed = unit_height_packed

    @property
    def unit_length_packed(self):
        """Gets the unit_length_packed of this Part.  # noqa: E501

        Indicate the Length packed (inch)  # noqa: E501

        :return: The unit_length_packed of this Part.  # noqa: E501
        :rtype: float
        """
        return self._unit_length_packed

    @unit_length_packed.setter
    def unit_length_packed(self, unit_length_packed):
        """Sets the unit_length_packed of this Part.

        Indicate the Length packed (inch)  # noqa: E501

        :param unit_length_packed: The unit_length_packed of this Part.  # noqa: E501
        :type: float
        """

        self._unit_length_packed = unit_length_packed

    @property
    def unit_width_packed(self):
        """Gets the unit_width_packed of this Part.  # noqa: E501

        Indicate the Width packed (inch)  # noqa: E501

        :return: The unit_width_packed of this Part.  # noqa: E501
        :rtype: float
        """
        return self._unit_width_packed

    @unit_width_packed.setter
    def unit_width_packed(self, unit_width_packed):
        """Sets the unit_width_packed of this Part.

        Indicate the Width packed (inch)  # noqa: E501

        :param unit_width_packed: The unit_width_packed of this Part.  # noqa: E501
        :type: float
        """

        self._unit_width_packed = unit_width_packed

    @property
    def unit_upc_code(self):
        """Gets the unit_upc_code of this Part.  # noqa: E501

        Indicate the UPC of this item  # noqa: E501

        :return: The unit_upc_code of this Part.  # noqa: E501
        :rtype: str
        """
        return self._unit_upc_code

    @unit_upc_code.setter
    def unit_upc_code(self, unit_upc_code):
        """Sets the unit_upc_code of this Part.

        Indicate the UPC of this item  # noqa: E501

        :param unit_upc_code: The unit_upc_code of this Part.  # noqa: E501
        :type: str
        """

        self._unit_upc_code = unit_upc_code

    @property
    def last_modification_date(self):
        """Gets the last_modification_date of this Part.  # noqa: E501


        :return: The last_modification_date of this Part.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_date

    @last_modification_date.setter
    def last_modification_date(self, last_modification_date):
        """Sets the last_modification_date of this Part.


        :param last_modification_date: The last_modification_date of this Part.  # noqa: E501
        :type: datetime
        """

        self._last_modification_date = last_modification_date

    @property
    def images(self):
        """Gets the images of this Part.  # noqa: E501

        List of all images associated with this item.  # noqa: E501

        :return: The images of this Part.  # noqa: E501
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Part.

        List of all images associated with this item.  # noqa: E501

        :param images: The images of this Part.  # noqa: E501
        :type: list[Image]
        """

        self._images = images

    @property
    def attributes(self):
        """Gets the attributes of this Part.  # noqa: E501

        List of all attributes associated with this item.  # noqa: E501

        :return: The attributes of this Part.  # noqa: E501
        :rtype: list[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Part.

        List of all attributes associated with this item.  # noqa: E501

        :param attributes: The attributes of this Part.  # noqa: E501
        :type: list[Attribute]
        """

        self._attributes = attributes

    @property
    def inventories(self):
        """Gets the inventories of this Part.  # noqa: E501

        List of all inventories associated with this item.  # noqa: E501

        :return: The inventories of this Part.  # noqa: E501
        :rtype: list[Inventory]
        """
        return self._inventories

    @inventories.setter
    def inventories(self, inventories):
        """Sets the inventories of this Part.

        List of all inventories associated with this item.  # noqa: E501

        :param inventories: The inventories of this Part.  # noqa: E501
        :type: list[Inventory]
        """

        self._inventories = inventories

    @property
    def categories(self):
        """Gets the categories of this Part.  # noqa: E501

        List of all categories associated with this item.  # noqa: E501

        :return: The categories of this Part.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Part.

        List of all categories associated with this item.  # noqa: E501

        :param categories: The categories of this Part.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

    @property
    def fitment_details(self):
        """Gets the fitment_details of this Part.  # noqa: E501


        :return: The fitment_details of this Part.  # noqa: E501
        :rtype: FitmentDetails
        """
        return self._fitment_details

    @fitment_details.setter
    def fitment_details(self, fitment_details):
        """Sets the fitment_details of this Part.


        :param fitment_details: The fitment_details of this Part.  # noqa: E501
        :type: FitmentDetails
        """

        self._fitment_details = fitment_details

    @property
    def related_parts(self):
        """Gets the related_parts of this Part.  # noqa: E501

        List of suggested related parts (ex: You might also like, Useful accessories ...)  # noqa: E501

        :return: The related_parts of this Part.  # noqa: E501
        :rtype: list[RelatedPart]
        """
        return self._related_parts

    @related_parts.setter
    def related_parts(self, related_parts):
        """Sets the related_parts of this Part.

        List of suggested related parts (ex: You might also like, Useful accessories ...)  # noqa: E501

        :param related_parts: The related_parts of this Part.  # noqa: E501
        :type: list[RelatedPart]
        """

        self._related_parts = related_parts

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
        if issubclass(Part, dict):
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
        if not isinstance(other, Part):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
