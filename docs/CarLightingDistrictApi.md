# swagger_client.CarLightingDistrictApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_car_lighting_district_vehicle_makes_vehicle_year_get**](CarLightingDistrictApi.md#api_car_lighting_district_vehicle_makes_vehicle_year_get) | **GET** /api/CarLightingDistrict/Vehicle/Makes/{VehicleYear} | Retrieves the makes of vehicles available for the CLD vehicle search according to the specified year.
[**api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get**](CarLightingDistrictApi.md#api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get) | **GET** /api/CarLightingDistrict/Vehicle/Models/{VehicleYear}/{VehicleMake} | Retrieves the models of vehicles available for the CLD vehicle search according to the specified year and make.
[**api_car_lighting_district_vehicle_parts_cld_vehicle_year_get**](CarLightingDistrictApi.md#api_car_lighting_district_vehicle_parts_cld_vehicle_year_get) | **GET** /api/CarLightingDistrict/VehiclePartsCLD/{VehicleYear} | Retrieves CLD parts for the specified vehicle
[**api_car_lighting_district_vehicle_years_get**](CarLightingDistrictApi.md#api_car_lighting_district_vehicle_years_get) | **GET** /api/CarLightingDistrict/Vehicle/Years | Retrieves the Years of vehicles available for the CLD vehicle search.

# **api_car_lighting_district_vehicle_makes_vehicle_year_get**
> list[str] api_car_lighting_district_vehicle_makes_vehicle_year_get(vehicle_year)

Retrieves the makes of vehicles available for the CLD vehicle search according to the specified year.

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **str**|  | 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get**
> list[str] api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get(vehicle_year, vehicle_make)

Retrieves the models of vehicles available for the CLD vehicle search according to the specified year and make.

### Example
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
vehicle_make = 'vehicle_make_example' # str | 

try:
    # Retrieves the models of vehicles available for the CLD vehicle search according to the specified year and make.
    api_response = api_instance.api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get(vehicle_year, vehicle_make)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_models_vehicle_year_vehicle_make_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **str**|  | 
 **vehicle_make** | **str**|  | 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_car_lighting_district_vehicle_parts_cld_vehicle_year_get**
> list[Part] api_car_lighting_district_vehicle_parts_cld_vehicle_year_get(vehicle_year, vehicle_make=vehicle_make, vehicle_model=vehicle_model)

Retrieves CLD parts for the specified vehicle

### Example
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
vehicle_year = 56 # int | 
vehicle_make = 'vehicle_make_example' # str |  (optional)
vehicle_model = 'vehicle_model_example' # str |  (optional)

try:
    # Retrieves CLD parts for the specified vehicle
    api_response = api_instance.api_car_lighting_district_vehicle_parts_cld_vehicle_year_get(vehicle_year, vehicle_make=vehicle_make, vehicle_model=vehicle_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_parts_cld_vehicle_year_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **int**|  | 
 **vehicle_make** | **str**|  | [optional] 
 **vehicle_model** | **str**|  | [optional] 

### Return type

[**list[Part]**](Part.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_car_lighting_district_vehicle_years_get**
> list[str] api_car_lighting_district_vehicle_years_get()

Retrieves the Years of vehicles available for the CLD vehicle search.

### Example
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

try:
    # Retrieves the Years of vehicles available for the CLD vehicle search.
    api_response = api_instance.api_car_lighting_district_vehicle_years_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarLightingDistrictApi->api_car_lighting_district_vehicle_years_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

