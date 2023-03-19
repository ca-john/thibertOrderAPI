# Part

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thibert_part_number** | **str** | Thibert part number associated with this item. | [optional] 
**your_price** | **float** | Price of this item for the given customer. | [optional] 
**your_price_currency_code** | **str** | Currency of YourPrice for the given customer. | [optional] 
**jobber_price** | [**list[PricesByCurrencies]**](PricesByCurrencies.md) | Jobber price of this item. | [optional] 
**msrp_price** | [**list[PricesByCurrencies]**](PricesByCurrencies.md) | Manufacturer&#x27;s suggested retail price of this item. | [optional] 
**map_price** | [**list[PricesByCurrencies]**](PricesByCurrencies.md) | Manufacturer&#x27;s suggested retail price of this item. | [optional] 
**vendor_part_number** | **str** | Manufacturer&#x27;s part number of this item. | [optional] 
**brand** | **str** | Brand associated with this item. | [optional] 
**model** | **str** | Model of this item. | [optional] 
**series** | **str** | Series of this item. | [optional] 
**web_status** | **str** | Availability status of this item. | [optional] 
**titles** | [**list[LocalizedString]**](LocalizedString.md) | Titles of this item. | [optional] 
**short_descriptions** | [**list[LocalizedString]**](LocalizedString.md) | Short description of this item. | [optional] 
**long_descriptions** | [**list[LocalizedString]**](LocalizedString.md) | Long description of this item. | [optional] 
**application_notes** | [**list[LocalizedString]**](LocalizedString.md) | Application note for the buyer. | [optional] 
**replacement_item** | **str** | Item which replaces this item. | [optional] 
**wheel_part_type_id** | **str** | WheelPartTypeID (00030 &#x3D; Dually, 00076 &#x3D; Styled Steel, 00021 &#x3D; Steel, 00020 &#x3D; Alloy) | [optional] 
**wheel_part_type** | [**list[LocalizedString]**](LocalizedString.md) | Wheel Part Type (Dually, Styled Steel, Steel, Alloy) in english and french | [optional] 
**is_on_clearance** | **bool** | Indicates if this part is on clearance | [optional] 
**is_on_clearance_title** | [**list[LocalizedString]**](LocalizedString.md) | Title of the Clearance | [optional] 
**is_new_arrival** | **bool** | Indicates if this part is a new arrival | [optional] 
**is_new_arrival_title** | [**list[LocalizedString]**](LocalizedString.md) | Title of the new arrival | [optional] 
**is_overweight** | **bool** | Indicates if this part is Overweight | [optional] 
**is_oversize** | **bool** | Indicates if this part is Oversize | [optional] 
**unit_net_weight_packed_lbs** | **float** | Indicate the unit weight packed (lbs) | [optional] 
**unit_height_packed** | **float** | Indicate the Height packed (inch) | [optional] 
**unit_length_packed** | **float** | Indicate the Length packed (inch) | [optional] 
**unit_width_packed** | **float** | Indicate the Width packed (inch) | [optional] 
**unit_upc_code** | **str** | Indicate the UPC of this item | [optional] 
**last_modification_date** | **datetime** |  | [optional] 
**images** | [**list[Image]**](Image.md) | List of all images associated with this item. | [optional] 
**attributes** | [**list[Attribute]**](Attribute.md) | List of all attributes associated with this item. | [optional] 
**inventories** | [**list[Inventory]**](Inventory.md) | List of all inventories associated with this item. | [optional] 
**categories** | [**list[Category]**](Category.md) | List of all categories associated with this item. | [optional] 
**fitment_details** | [**FitmentDetails**](FitmentDetails.md) |  | [optional] 
**related_parts** | [**list[RelatedPart]**](RelatedPart.md) | List of suggested related parts (ex: You might also like, Useful accessories ...) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

