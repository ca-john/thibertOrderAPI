# swagger_client.FitmentTireGuideApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_fitment_tire_guide_parts_part_type_post**](FitmentTireGuideApi.md#api_fitment_tire_guide_parts_part_type_post) | **POST** /api/FitmentTireGuide/Parts/{PartType} | Retrieves the parts fitting the provided Vehicle CarTireID. If the CarTireID is not provided, retrieves parts without fitment for a specific car.
[**api_fitment_tire_guide_wheel_filter_bolt_pattern_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_bolt_pattern_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/BoltPattern | Retrieves all available Bolt Pattern or all available Bolt Pattern for a vehicle based on the CarTireID.
[**api_fitment_tire_guide_wheel_filter_brands_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_brands_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Brands | Retrieves all available Brands or all available Brands for a vehicle based on the CarTireID.
[**api_fitment_tire_guide_wheel_filter_center_bore_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_center_bore_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/CenterBore | Retrieves all available Center Bore or all available Center Bore for a vehicle based on the CarTireID.
[**api_fitment_tire_guide_wheel_filter_diameter_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_diameter_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Diameter | Retrieves all available Diameter or all available Diameter for a vehicle based on the CarTireID.
[**api_fitment_tire_guide_wheel_filter_offset_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_offset_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Offset | Retrieves all available Offset or all available Offset for a vehicle based on the CarTireID.
[**api_fitment_tire_guide_wheel_filter_wheel_part_type_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_wheel_part_type_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/WheelPartType | Retrieves all available WheelPartType or all available WheelPartType for a vehicle based on the CarTireID.
[**api_fitment_tire_guide_wheel_filter_width_get**](FitmentTireGuideApi.md#api_fitment_tire_guide_wheel_filter_width_get) | **GET** /api/FitmentTireGuide/Wheel/Filter/Width | Retrieves all available Width or all available Width for a vehicle based on the CarTireID.

# **api_fitment_tire_guide_parts_part_type_post**
> list[Part] api_fitment_tire_guide_parts_part_type_post(part_type, body=body, car_tire_id=car_tire_id, page_number=page_number, page_size=page_size)

Retrieves the parts fitting the provided Vehicle CarTireID. If the CarTireID is not provided, retrieves parts without fitment for a specific car.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
part_type = 'part_type_example' # str | Type of parts searched. Wheels, Accessories or both. Values: 1 (Wheels), 2 (Accessories), 3 (Wheels and Accessories)
body = swagger_client.PartsFilters() # PartsFilters | Allows to filter the search result. (optional)
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves the parts fitting the provided Vehicle CarTireID. If the CarTireID is not provided, retrieves parts without fitment for a specific car.
    api_response = api_instance.api_fitment_tire_guide_parts_part_type_post(part_type, body=body, car_tire_id=car_tire_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_parts_part_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_type** | **str**| Type of parts searched. Wheels, Accessories or both. Values: 1 (Wheels), 2 (Accessories), 3 (Wheels and Accessories) | 
 **body** | [**PartsFilters**](PartsFilters.md)| Allows to filter the search result. | [optional] 
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 
 **page_number** | **int**| Number of the page to retrieve. Default value: 1 | [optional] 
 **page_size** | **int**| Number of results per page. Default value: 50, Maximum allowed: 200 | [optional] 

### Return type

[**list[Part]**](Part.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_bolt_pattern_get**
> list[str] api_fitment_tire_guide_wheel_filter_bolt_pattern_get(car_tire_id=car_tire_id)

Retrieves all available Bolt Pattern or all available Bolt Pattern for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available Bolt Pattern or all available Bolt Pattern for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_bolt_pattern_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_bolt_pattern_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_brands_get**
> list[str] api_fitment_tire_guide_wheel_filter_brands_get(car_tire_id=car_tire_id)

Retrieves all available Brands or all available Brands for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available Brands or all available Brands for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_brands_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_brands_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_center_bore_get**
> list[str] api_fitment_tire_guide_wheel_filter_center_bore_get(car_tire_id=car_tire_id)

Retrieves all available Center Bore or all available Center Bore for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available Center Bore or all available Center Bore for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_center_bore_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_center_bore_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_diameter_get**
> list[str] api_fitment_tire_guide_wheel_filter_diameter_get(car_tire_id=car_tire_id)

Retrieves all available Diameter or all available Diameter for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available Diameter or all available Diameter for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_diameter_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_diameter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_offset_get**
> list[str] api_fitment_tire_guide_wheel_filter_offset_get(car_tire_id=car_tire_id)

Retrieves all available Offset or all available Offset for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available Offset or all available Offset for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_offset_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_offset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_wheel_part_type_get**
> list[WheelPartType] api_fitment_tire_guide_wheel_filter_wheel_part_type_get(car_tire_id=car_tire_id)

Retrieves all available WheelPartType or all available WheelPartType for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available WheelPartType or all available WheelPartType for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_wheel_part_type_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_wheel_part_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

[**list[WheelPartType]**](WheelPartType.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_tire_guide_wheel_filter_width_get**
> list[str] api_fitment_tire_guide_wheel_filter_width_get(car_tire_id=car_tire_id)

Retrieves all available Width or all available Width for a vehicle based on the CarTireID.

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
api_instance = swagger_client.FitmentTireGuideApi(swagger_client.ApiClient(configuration))
car_tire_id = 'car_tire_id_example' # str | Tire Guide vehicle ID to look up with. (optional)

try:
    # Retrieves all available Width or all available Width for a vehicle based on the CarTireID.
    api_response = api_instance.api_fitment_tire_guide_wheel_filter_width_get(car_tire_id=car_tire_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentTireGuideApi->api_fitment_tire_guide_wheel_filter_width_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_tire_id** | **str**| Tire Guide vehicle ID to look up with. | [optional] 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

