# swagger_client.InventoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_inventory_all_inventory_get**](InventoryApi.md#api_inventory_all_inventory_get) | **GET** /api/Inventory/AllInventory | Retrieves inventory for specified parts
[**api_inventory_part_inventory_get**](InventoryApi.md#api_inventory_part_inventory_get) | **GET** /api/Inventory/PartInventory | Retrieves inventory for specified parts

# **api_inventory_all_inventory_get**
> list[PartInventory] api_inventory_all_inventory_get(page_number=page_number, page_size=page_size)

Retrieves inventory for specified parts

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
api_instance = swagger_client.InventoryApi(swagger_client.ApiClient(configuration))
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves inventory for specified parts
    api_response = api_instance.api_inventory_all_inventory_get(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->api_inventory_all_inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Number of the page to retrieve. Default value: 1 | [optional] 
 **page_size** | **int**| Number of results per page. Default value: 50, Maximum allowed: 200 | [optional] 

### Return type

[**list[PartInventory]**](PartInventory.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_inventory_part_inventory_get**
> list[Inventory] api_inventory_part_inventory_get(thibert_part_numbers=thibert_part_numbers, page_number=page_number, page_size=page_size)

Retrieves inventory for specified parts

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
api_instance = swagger_client.InventoryApi(swagger_client.ApiClient(configuration))
thibert_part_numbers = ['thibert_part_numbers_example'] # list[str] |  (optional)
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves inventory for specified parts
    api_response = api_instance.api_inventory_part_inventory_get(thibert_part_numbers=thibert_part_numbers, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->api_inventory_part_inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thibert_part_numbers** | [**list[str]**](str.md)|  | [optional] 
 **page_number** | **int**| Number of the page to retrieve. Default value: 1 | [optional] 
 **page_size** | **int**| Number of results per page. Default value: 50, Maximum allowed: 200 | [optional] 

### Return type

[**list[Inventory]**](Inventory.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

