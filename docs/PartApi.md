# swagger_client.PartApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_part_post**](PartApi.md#api_part_post) | **POST** /api/Part | Retrieves detailed part information according to the filters provided. If no filter is provided, retrieves the entire customer catalog.

# **api_part_post**
> list[Part] api_part_post(body=body, part_type=part_type, page_number=page_number, page_size=page_size)

Retrieves detailed part information according to the filters provided. If no filter is provided, retrieves the entire customer catalog.

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
api_instance = swagger_client.PartApi(swagger_client.ApiClient(configuration))
body = swagger_client.PartsFilters() # PartsFilters | Allows to filter the search result.
<br />
Available filters name: ThibertPartNumber, VendorPartNumber, WheelPartTypeID, Brand, Diameter, Width, BoltPattern, CenterBore, Offset, CategoryId, LastModificationDate.
<br />
Example of possible filter values (not exhaustive)
<br />
ThibertPartNumber: 081001, 00021, 00030, 00076
<br />
VendorPartNumber: 32571885114342731MM1, 49581, 8LTC49K
<br />
WheelPartTypeID: 00020, 00021, 00030, 00076
<br />
Brand: RTX, Ceco, Black Rhino ...
<br />
Diameter: 17, 18, 19 ...
<br />
Width: 6, 8, 9.5 ...
<br />
BoltPattern: 5x114.3, 6x132, 8x165.1 ...
<br />
CenterBore: 60.1, 108, 130.8
<br />
Offset: -13, 27, 52.5
<br />
CategoryId: 0360, 026 ...
<br />
LastModificationDate: 12/31/2023 (optional)
part_type = 'part_type_example' # str | Type of parts searched. Wheels, Accessories or both. Values: 1 (Wheels), 2 (Accessories), 3 (Wheels and Accessories) (optional)
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves detailed part information according to the filters provided. If no filter is provided, retrieves the entire customer catalog.
    api_response = api_instance.api_part_post(body=body, part_type=part_type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartApi->api_part_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartsFilters**](PartsFilters.md)| Allows to filter the search result.
&lt;br /&gt;
Available filters name: ThibertPartNumber, VendorPartNumber, WheelPartTypeID, Brand, Diameter, Width, BoltPattern, CenterBore, Offset, CategoryId, LastModificationDate.
&lt;br /&gt;
Example of possible filter values (not exhaustive)
&lt;br /&gt;
ThibertPartNumber: 081001, 00021, 00030, 00076
&lt;br /&gt;
VendorPartNumber: 32571885114342731MM1, 49581, 8LTC49K
&lt;br /&gt;
WheelPartTypeID: 00020, 00021, 00030, 00076
&lt;br /&gt;
Brand: RTX, Ceco, Black Rhino ...
&lt;br /&gt;
Diameter: 17, 18, 19 ...
&lt;br /&gt;
Width: 6, 8, 9.5 ...
&lt;br /&gt;
BoltPattern: 5x114.3, 6x132, 8x165.1 ...
&lt;br /&gt;
CenterBore: 60.1, 108, 130.8
&lt;br /&gt;
Offset: -13, 27, 52.5
&lt;br /&gt;
CategoryId: 0360, 026 ...
&lt;br /&gt;
LastModificationDate: 12/31/2023 | [optional] 
 **part_type** | **str**| Type of parts searched. Wheels, Accessories or both. Values: 1 (Wheels), 2 (Accessories), 3 (Wheels and Accessories) | [optional] 
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

