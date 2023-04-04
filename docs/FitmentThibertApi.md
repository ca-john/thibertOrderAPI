# swagger_client.FitmentThibertApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_fitment_thibert_vehicle_makes_vehicle_year_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_makes_vehicle_year_get) | **GET** /api/FitmentThibert/VehicleMakes/{VehicleYear} | Retrieves the makes of vehicles available for the Thibert vehicle search according to the specified year.
[**api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get) | **GET** /api/FitmentThibert/VehicleModels/{VehicleYear}/{VehicleMake} | Retrieves the models of vehicles available for the Thibert vehicle search according to the specified year and make.
[**api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get) | **GET** /api/FitmentThibert/VehicleOptions/{VehicleYear}/{VehicleMake}/{VehicleModel}/{VehicleSubModel} | Retrieves the options of vehicles available for the Thibert vehicle search according to the specified year, make, model and sub model.
[**api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get) | **GET** /api/FitmentThibert/VehicleParts/InstallationKitsByVehicle/{VehicleYear}/{VehicleMake}/{VehicleModel}/{VehicleSubModel} | Retrieves all installations kits for the vehicle and part specified
[**api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get) | **GET** /api/FitmentThibert/VehicleParts/InstallationPartsByVehicle/{VehicleYear}/{VehicleMake}/{VehicleModel}/{VehicleSubModel} | Retrieves all installations parts AND kits for the vehicle and part specified
[**api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post**](FitmentThibertApi.md#api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post) | **POST** /api/FitmentThibert/VehicleParts/{SearchType}/{VehicleYear}/{VehicleMake}/{VehicleModel} | Retrieves parts suitable for the specified Thibert vehicle
[**api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get) | **GET** /api/FitmentThibert/VehicleSubModels/{VehicleYear}/{VehicleMake}/{VehicleModel} | Retrieves the sub models of vehicles available for the Thibert vehicle search according to the specified year, make and model.
[**api_fitment_thibert_vehicle_years_get**](FitmentThibertApi.md#api_fitment_thibert_vehicle_years_get) | **GET** /api/FitmentThibert/VehicleYears | Retrieves the Years of vehicles available for the Thibert vehicle search.

# **api_fitment_thibert_vehicle_makes_vehicle_year_get**
> list[str] api_fitment_thibert_vehicle_makes_vehicle_year_get(vehicle_year)

Retrieves the makes of vehicles available for the Thibert vehicle search according to the specified year.

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 

try:
    # Retrieves the makes of vehicles available for the Thibert vehicle search according to the specified year.
    api_response = api_instance.api_fitment_thibert_vehicle_makes_vehicle_year_get(vehicle_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_makes_vehicle_year_get: %s\n" % e)
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

# **api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get**
> list[str] api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get(vehicle_year, vehicle_make)

Retrieves the models of vehicles available for the Thibert vehicle search according to the specified year and make.

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 
vehicle_make = 'vehicle_make_example' # str | 

try:
    # Retrieves the models of vehicles available for the Thibert vehicle search according to the specified year and make.
    api_response = api_instance.api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get(vehicle_year, vehicle_make)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_models_vehicle_year_vehicle_make_get: %s\n" % e)
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

# **api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**
> list[str] api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get(vehicle_year, vehicle_make, vehicle_model, vehicle_sub_model)

Retrieves the options of vehicles available for the Thibert vehicle search according to the specified year, make, model and sub model.

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 
vehicle_make = 'vehicle_make_example' # str | 
vehicle_model = 'vehicle_model_example' # str | 
vehicle_sub_model = 'vehicle_sub_model_example' # str | 

try:
    # Retrieves the options of vehicles available for the Thibert vehicle search according to the specified year, make, model and sub model.
    api_response = api_instance.api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get(vehicle_year, vehicle_make, vehicle_model, vehicle_sub_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_options_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **str**|  | 
 **vehicle_make** | **str**|  | 
 **vehicle_model** | **str**|  | 
 **vehicle_sub_model** | **str**|  | 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**
> WheelInstallation api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get(vehicle_year, vehicle_make, vehicle_model, vehicle_sub_model, vehicle_option=vehicle_option, rt_part_number=rt_part_number)

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 
vehicle_make = 'vehicle_make_example' # str | 
vehicle_model = 'vehicle_model_example' # str | 
vehicle_sub_model = 'vehicle_sub_model_example' # str | 
vehicle_option = 'vehicle_option_example' # str |  (optional)
rt_part_number = 'rt_part_number_example' # str |  (optional)

try:
    # Retrieves all installations kits for the vehicle and part specified
    api_response = api_instance.api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get(vehicle_year, vehicle_make, vehicle_model, vehicle_sub_model, vehicle_option=vehicle_option, rt_part_number=rt_part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_parts_installation_kits_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **str**|  | 
 **vehicle_make** | **str**|  | 
 **vehicle_model** | **str**|  | 
 **vehicle_sub_model** | **str**|  | 
 **vehicle_option** | **str**|  | [optional] 
 **rt_part_number** | **str**|  | [optional] 

### Return type

[**WheelInstallation**](WheelInstallation.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get**
> WheelInstallation api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get(vehicle_year, vehicle_make, vehicle_model, vehicle_sub_model, vehicle_option=vehicle_option, rt_part_number=rt_part_number)

Retrieves all installations parts AND kits for the vehicle and part specified

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 
vehicle_make = 'vehicle_make_example' # str | 
vehicle_model = 'vehicle_model_example' # str | 
vehicle_sub_model = 'vehicle_sub_model_example' # str | 
vehicle_option = 'vehicle_option_example' # str |  (optional)
rt_part_number = 'rt_part_number_example' # str |  (optional)

try:
    # Retrieves all installations parts AND kits for the vehicle and part specified
    api_response = api_instance.api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get(vehicle_year, vehicle_make, vehicle_model, vehicle_sub_model, vehicle_option=vehicle_option, rt_part_number=rt_part_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_parts_installation_parts_by_vehicle_vehicle_year_vehicle_make_vehicle_model_vehicle_sub_model_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **str**|  | 
 **vehicle_make** | **str**|  | 
 **vehicle_model** | **str**|  | 
 **vehicle_sub_model** | **str**|  | 
 **vehicle_option** | **str**|  | [optional] 
 **rt_part_number** | **str**|  | [optional] 

### Return type

[**WheelInstallation**](WheelInstallation.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post**
> list[Part] api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post(search_type, vehicle_year, vehicle_make, vehicle_model, body=body, vehicle_sub_model=vehicle_sub_model, vehicle_option=vehicle_option, page_number=page_number, page_size=page_size)

Retrieves parts suitable for the specified Thibert vehicle

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
search_type = 56 # int | Indicates the type of search. Wheels, Accessories or both. Values: 1 (Wheels), 2 (Accessories), 3 (Wheels and Accessories)
vehicle_year = 56 # int | 
vehicle_make = 'vehicle_make_example' # str | 
vehicle_model = 'vehicle_model_example' # str | 
body = swagger_client.PartsFilters() # PartsFilters |  (optional)
vehicle_sub_model = 'vehicle_sub_model_example' # str | *** Optional for SearchType 2 (Accessories) only (optional)
vehicle_option = 'vehicle_option_example' # str | *** Optional (optional)
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves parts suitable for the specified Thibert vehicle
    api_response = api_instance.api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post(search_type, vehicle_year, vehicle_make, vehicle_model, body=body, vehicle_sub_model=vehicle_sub_model, vehicle_option=vehicle_option, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_parts_search_type_vehicle_year_vehicle_make_vehicle_model_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_type** | **int**| Indicates the type of search. Wheels, Accessories or both. Values: 1 (Wheels), 2 (Accessories), 3 (Wheels and Accessories) | 
 **vehicle_year** | **int**|  | 
 **vehicle_make** | **str**|  | 
 **vehicle_model** | **str**|  | 
 **body** | [**PartsFilters**](PartsFilters.md)|  | [optional] 
 **vehicle_sub_model** | **str**| *** Optional for SearchType 2 (Accessories) only | [optional] 
 **vehicle_option** | **str**| *** Optional | [optional] 
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

# **api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get**
> list[str] api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get(vehicle_year, vehicle_make, vehicle_model)

Retrieves the sub models of vehicles available for the Thibert vehicle search according to the specified year, make and model.

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))
vehicle_year = 'vehicle_year_example' # str | 
vehicle_make = 'vehicle_make_example' # str | 
vehicle_model = 'vehicle_model_example' # str | 

try:
    # Retrieves the sub models of vehicles available for the Thibert vehicle search according to the specified year, make and model.
    api_response = api_instance.api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get(vehicle_year, vehicle_make, vehicle_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_sub_models_vehicle_year_vehicle_make_vehicle_model_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_year** | **str**|  | 
 **vehicle_make** | **str**|  | 
 **vehicle_model** | **str**|  | 

### Return type

**list[str]**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_fitment_thibert_vehicle_years_get**
> list[str] api_fitment_thibert_vehicle_years_get()

Retrieves the Years of vehicles available for the Thibert vehicle search.

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
api_instance = swagger_client.FitmentThibertApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the Years of vehicles available for the Thibert vehicle search.
    api_response = api_instance.api_fitment_thibert_vehicle_years_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FitmentThibertApi->api_fitment_thibert_vehicle_years_get: %s\n" % e)
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

