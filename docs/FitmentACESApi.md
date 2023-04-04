# swagger_client.FitmentACESApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_fitment_aces_part_aces_vehicle_id_get**](FitmentACESApi.md#api_fitment_aces_part_aces_vehicle_id_get) | **GET** /api/FitmentACES/Part/{AcesVehicleID} | Retrieves the parts fitting the provided ACES vehicle ID.
[**api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get**](FitmentACESApi.md#api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get) | **GET** /api/FitmentACES/VehicleParts/InstallationKitsByVehicle/{AcesVehicleID} | Retrieves all installations kits for the vehicle and part specified

# **api_fitment_aces_part_aces_vehicle_id_get**
> list[Part] api_fitment_aces_part_aces_vehicle_id_get(aces_vehicle_id, page_number=page_number, page_size=page_size)

Retrieves the parts fitting the provided ACES vehicle ID.

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
api_instance = swagger_client.FitmentACESApi(swagger_client.ApiClient(configuration))
aces_vehicle_id = 'aces_vehicle_id_example' # str | ACES vehicle ID to look up with.
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves the parts fitting the provided ACES vehicle ID.
    api_response = api_instance.api_fitment_aces_part_aces_vehicle_id_get(aces_vehicle_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentACESApi->api_fitment_aces_part_aces_vehicle_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aces_vehicle_id** | **str**| ACES vehicle ID to look up with. | 
 **page_number** | **int**| Number of the page to retrieve. Default value: 1 | [optional] 
 **page_size** | **int**| Number of results per page. Default value: 50, Maximum allowed: 200 | [optional] 

### Return type

[**list[Part]**](Part.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get**
> WheelInstallation api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get(aces_vehicle_id, rt_part_number=rt_part_number)

Retrieves all installations kits for the vehicle and part specified

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
api_instance = swagger_client.FitmentACESApi(swagger_client.ApiClient(configuration))
aces_vehicle_id = 'aces_vehicle_id_example' # str | 
rt_part_number = 'rt_part_number_example' # str |  (optional)

try:
    # Retrieves all installations kits for the vehicle and part specified
    api_response = api_instance.api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get(aces_vehicle_id, rt_part_number=rt_part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentACESApi->api_fitment_aces_vehicle_parts_installation_kits_by_vehicle_aces_vehicle_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aces_vehicle_id** | **str**|  | 
 **rt_part_number** | **str**|  | [optional] 

### Return type

[**WheelInstallation**](WheelInstallation.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

