# thibert-client

- API version: V1 DEVELOPMENT
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

Install requirements.

```sh
pip3 install -r requirements.txt
```

## Getting Started
After installing the prerequisites, create a cred.py file with the required API key and base URL for the endpoints.

Run the following to start the order.
```
python thibert.py
```
Input the information into the CLI and wait for the submission.

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TAPI Key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CarLightingDistrictApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 

try:
    # Retrieves the makes of vehicles available for the CLD vehicle search according to the specified year.
    api_response = api_instance.api_car_lighting_district_vehicle_makes_vehicle_year_get(vehicle_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_makes_vehicle_year_get: %s\n" % e)

# Configure API key authorization: TAPI Key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CarLightingDistrictApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 
vehicle_make = 'vehicle_make_example' # str | 

try:
    # Retrieves the models of vehicles available for the CLD vehicle search according to the specified year and make.
    api_response = api_instance.api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get(vehicle_year, vehicle_make)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get: %s\n" % e)

# Configure API key authorization: TAPI Key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CarLightingDistrictApi(swagger_client.ApiClient(configuration))
vehicle_year = 56 # int | 
vehicle_make = 'vehicle_make_example' # str |  (optional)
vehicle_model = 'vehicle_model_example' # str |  (optional)

try:
    # Retrieves CLD parts for the specified vehicle
    api_response = api_instance.api_car_lighting_district_vehicle_parts_cld_vehicle_year_get(vehicle_year, vehicle_make=vehicle_make, vehicle_model=vehicle_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_parts_cld_vehicle_year_get: %s\n" % e)

# Configure API key authorization: TAPI Key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CarLightingDistrictApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the Years of vehicles available for the CLD vehicle search.
    api_response = api_instance.api_car_lighting_district_vehicle_years_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_years_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CarLightingDistrictApi* | [**api_car_lighting_district_vehicle_makes_vehicle_year_get**](docs/CarLightingDistrictApi.md#api_car_lighting_district_vehicle_makes_vehicle_year_get) | **GET** /api/CarLightingDistrict/Vehicle/Makes/{VehicleYear} | Retrieves the makes of vehicles available for the CLD vehicle search according to the specified year.
*CarLightingDistrictApi* | [**api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get**](docs/CarLightingDistrictApi.md#api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get) | **GET** /api/CarLightingDistrict/Vehicle/Models/{VehicleYear}/{VehicleMake} | Retrieves the models of vehicles available for the CLD vehicle search according to the specified year and make.
*CarLightingDistrictApi* | [**api_car_lighting_district_vehicle_parts_cld_vehicle_year_get**](docs/CarLightingDistrictApi.md#api_car_lighting_district_vehicle_parts_cld_vehicle_year_get) | **GET** /api/CarLightingDistrict/VehiclePartsCLD/{VehicleYear} | Retrieves CLD parts for the specified vehicle
*CarLightingDistrictApi* | [**api_car_lighting_district_vehicle_years_get**](docs/CarLightingDistrictApi.md#api_car_lighting_district_vehicle_years_get) | **GET** /api/CarLightingDistrict/Vehicle/Years | Retrieves the Years of vehicles available for the CLD vehicle search.
*CategoriesApi* | [**api_categories_all_categories_get**](docs/CategoriesApi.md#api_categories_all_categories_get) | **GET** /api/Categories/AllCategories | Retrieves all the Thibert categories hierarchy
*FitmentACESApi* | [**api_fitment_aces_part_aces_vehicle_id_get**](docs/FitmentACESApi.md#api_fitment_aces_part_aces_vehicle_id_get) | **GET** /api/FitmentACES/Part/{AcesVehicleID} | Retrieves the parts fitting the provided ACES vehicle ID.
*FitmentACESApi* | [**api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get**](docs/FitmentACESApi.md#api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get) | **GET** /api/FitmentACES/VehicleParts/InstallationKitsByVehicle/{AcesVehicleID} | Retrieves all installations kits for the vehicle and part specified
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_makes_vehicle_year_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_makes_vehicle_year_get) | **GET** /api/FitmentThibert/VehicleMakes/{VehicleYear} | Retrieves the makes of vehicles available for the Thibert vehicle search according to the specified year.
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get) | **GET** /api/FitmentThibert/VehicleModels/{VehicleYear}/{VehicleMake} | Retrieves the models of vehicles available for the Thibert vehicle search according to the specified year and make.
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get) | **GET** /api/FitmentThibert/VehicleOptions/{VehicleYear}/{VehicleMake}/{VehicleModel}/{VehicleSubModel} | Retrieves the options of vehicles available for the Thibert vehicle search according to the specified year, make, model and sub model.
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get) | **GET** /api/FitmentThibert/VehicleParts/InstallationKitsByVehicle/{VehicleYear}/{VehicleMake}/{VehicleModel}/{VehicleSubModel} | Retrieves all installations kits for the vehicle and part specified
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get) | **GET** /api/FitmentThibert/VehicleParts/InstallationPartsByVehicle/{VehicleYear}/{VehicleMake}/{VehicleModel}/{VehicleSubModel} | Retrieves all installations parts AND kits for the vehicle and part specified
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post) | **POST** /api/FitmentThibert/VehicleParts/{SearchType}/{VehicleYear}/{VehicleMake}/{VehicleModel} | Retrieves parts suitable for the specified Thibert vehicle
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get) | **GET** /api/FitmentThibert/VehicleSubModels/{VehicleYear}/{VehicleMake}/{VehicleModel} | Retrieves the sub models of vehicles available for the Thibert vehicle search according to the specified year, make and model.
*FitmentThibertApi* | [**api_fitment_thibert_vehicle_years_get**](docs/FitmentThibertApi.md#api_fitment_thibert_vehicle_years_get) | **GET** /api/FitmentThibert/VehicleYears | Retrieves the Years of vehicles available for the Thibert vehicle search.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_parts_part_type_post**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_parts_part_type_post) | **POST** /api/FitmentTireGuide/Parts/{PartType} | Retrieves the parts fitting the provided Vehicle CarTireID. If the CarTireID is not provided, retrieves parts without fitment for a specific car.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_bolt_pattern_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_bolt_pattern_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/BoltPattern | Retrieves all available Bolt Pattern or all available Bolt Pattern for a vehicle based on the CarTireID.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_brands_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_brands_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Brands | Retrieves all available Brands or all available Brands for a vehicle based on the CarTireID.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_center_bore_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_center_bore_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/CenterBore | Retrieves all available Center Bore or all available Center Bore for a vehicle based on the CarTireID.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_diameter_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_diameter_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Diameter | Retrieves all available Diameter or all available Diameter for a vehicle based on the CarTireID.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_offset_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_offset_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Offset | Retrieves all available Offset or all available Offset for a vehicle based on the CarTireID.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_wheel_part_type_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_wheel_part_type_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/WheelPartType | Retrieves all available WheelPartType or all available WheelPartType for a vehicle based on the CarTireID.
*FitmentTireGuideApi* | [**api_fitment_tire_guide_wheel_filter_width_get**](docs/FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_width_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Width | Retrieves all available Width or all available Width for a vehicle based on the CarTireID.
*InventoryApi* | [**api_inventory_all_inventory_get**](docs/InventoryApi.md#api_inventory_all_inventory_get) | **GET** /api/Inventory/AllInventory | Retrieves inventory for specified parts
*InventoryApi* | [**api_inventory_part_inventory_get**](docs/InventoryApi.md#api_inventory_part_inventory_get) | **GET** /api/Inventory/PartInventory | Retrieves inventory for specified parts
*OrderApi* | [**api_order_invoice_pdf_get**](docs/OrderApi.md#api_order_invoice_pdf_get) | **GET** /api/Order/InvoicePDF | Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller&#x27;s side.
*OrderApi* | [**api_order_invoices_get**](docs/OrderApi.md#api_order_invoices_get) | **GET** /api/Order/Invoices | Retrieves invoices associated to the account in pages of 10.
*OrderApi* | [**api_order_order_status_post**](docs/OrderApi.md#api_order_order_status_post) | **POST** /api/Order/OrderStatus | Retrieves the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.
*OrderApi* | [**api_order_post**](docs/OrderApi.md#api_order_post) | **POST** /api/Order | Processes an order in our systems.
*OrderApi* | [**api_order_tracking_number_post**](docs/OrderApi.md#api_order_tracking_number_post) | **POST** /api/Order/TrackingNumber | Retrieves the tracking numbers associated with the specified orders
*PartApi* | [**api_part_post**](docs/PartApi.md#api_part_post) | **POST** /api/Part | Retrieves detailed part information according to the filters provided. If no filter is provided, retrieves the entire customer catalog.

## Documentation For Models

 - [Address](docs/Address.md)
 - [Attribute](docs/Attribute.md)
 - [Category](docs/Category.md)
 - [Contact](docs/Contact.md)
 - [DiameterFilter](docs/DiameterFilter.md)
 - [FilterLine](docs/FilterLine.md)
 - [FilterTags](docs/FilterTags.md)
 - [FitmentDetails](docs/FitmentDetails.md)
 - [Image](docs/Image.md)
 - [Inventory](docs/Inventory.md)
 - [Invoice](docs/Invoice.md)
 - [LocalizedString](docs/LocalizedString.md)
 - [Order](docs/Order.md)
 - [OrderConfirmation](docs/OrderConfirmation.md)
 - [OrderLine](docs/OrderLine.md)
 - [OrderStatus](docs/OrderStatus.md)
 - [OrderTracking](docs/OrderTracking.md)
 - [Part](docs/Part.md)
 - [PartInventory](docs/PartInventory.md)
 - [PartIsVehicleSpecific](docs/PartIsVehicleSpecific.md)
 - [PartsFilters](docs/PartsFilters.md)
 - [PricesByCurrencies](docs/PricesByCurrencies.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [RelatedPart](docs/RelatedPart.md)
 - [Salesline](docs/Salesline.md)
 - [TaskCreationRequest](docs/TaskCreationRequest.md)
 - [TaskItem](docs/TaskItem.md)
 - [Taxline](docs/Taxline.md)
 - [WheelInstallation](docs/WheelInstallation.md)
 - [WheelInstallationKit](docs/WheelInstallationKit.md)
 - [WheelInstallationPart](docs/WheelInstallationPart.md)
 - [WheelPartType](docs/WheelPartType.md)

## Documentation For Authorization


## TAPI Key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author
Momin Naseem

