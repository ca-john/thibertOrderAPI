# swagger_client.CategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_categories_all_categories_get**](CategoriesApi.md#api_categories_all_categories_get) | **GET** /api/Categories/AllCategories | Retrieves all the Thibert categories hierarchy

# **api_categories_all_categories_get**
> list[Category] api_categories_all_categories_get()

Retrieves all the Thibert categories hierarchy

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves all the Thibert categories hierarchy
    api_response = api_instance.api_categories_all_categories_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->api_categories_all_categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Category]**](Category.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

