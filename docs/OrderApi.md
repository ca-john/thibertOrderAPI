# swagger_client.OrderApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_order_invoice_pdf_get**](OrderApi.md#api_order_invoice_pdf_get) | **GET** /api/Order/InvoicePDF | Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller&#x27;s side.
[**api_order_invoices_get**](OrderApi.md#api_order_invoices_get) | **GET** /api/Order/Invoices | Retrieves invoices associated to the account in pages of 10.
[**api_order_order_status_post**](OrderApi.md#api_order_order_status_post) | **POST** /api/Order/OrderStatus | Retrieves the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.
[**api_order_post**](OrderApi.md#api_order_post) | **POST** /api/Order | Processes an order in our systems.
[**api_order_tracking_number_post**](OrderApi.md#api_order_tracking_number_post) | **POST** /api/Order/TrackingNumber | Retrieves the tracking numbers associated with the specified orders

# **api_order_invoice_pdf_get**
> str api_order_invoice_pdf_get(invoice_id=invoice_id, original_order_id=original_order_id)

Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller's side.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | Invoice number (optional)
original_order_id = 'original_order_id_example' # str | Order number related to the specified invoice (optional)

try:
    # Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller's side.
    api_response = api_instance.api_order_invoice_pdf_get(invoice_id=invoice_id, original_order_id=original_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->api_order_invoice_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| Invoice number | [optional] 
 **original_order_id** | **str**| Order number related to the specified invoice | [optional] 

### Return type

**str**

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_order_invoices_get**
> list[Invoice] api_order_invoices_get(start_date=start_date, end_date=end_date, page=page)

Retrieves invoices associated to the account in pages of 10.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter invoices by start date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter invoices by end date (optional)
page = 56 # int | Page to retrieve (optional)

try:
    # Retrieves invoices associated to the account in pages of 10.
    api_response = api_instance.api_order_invoices_get(start_date=start_date, end_date=end_date, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->api_order_invoices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| Filter invoices by start date | [optional] 
 **end_date** | **datetime**| Filter invoices by end date | [optional] 
 **page** | **int**| Page to retrieve | [optional] 

### Return type

[**list[Invoice]**](Invoice.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_order_order_status_post**
> list[OrderStatus] api_order_order_status_post(body=body, order_number_type=order_number_type, page_number=page_number, page_size=page_size)

Retrieves the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = ['[ \"CO0009997\", \"CO0009998\", \"CO0009999\", \"...\" ]'] # list[str] | List of order numbers base on the OrderType (optional)
order_number_type = 56 # int | Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference) (optional)
page_number = 56 # int | Number of the page to retrieve. Default value: 1 (optional)
page_size = 56 # int | Number of results per page. Default value: 50, Maximum allowed: 200 (optional)

try:
    # Retrieves the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.
    api_response = api_instance.api_order_order_status_post(body=body, order_number_type=order_number_type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->api_order_order_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| List of order numbers base on the OrderType | [optional] 
 **order_number_type** | **int**| Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference) | [optional] 
 **page_number** | **int**| Number of the page to retrieve. Default value: 1 | [optional] 
 **page_size** | **int**| Number of results per page. Default value: 50, Maximum allowed: 200 | [optional] 

### Return type

[**list[OrderStatus]**](OrderStatus.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_order_post**
> OrderConfirmation api_order_post(body=body)

Processes an order in our systems.

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = swagger_client.Order() # Order | Order to be saved. (optional)

try:
    # Processes an order in our systems.
    api_response = api_instance.api_order_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->api_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)| Order to be saved. | [optional] 

### Return type

[**OrderConfirmation**](OrderConfirmation.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_order_tracking_number_post**
> list[OrderTracking] api_order_tracking_number_post(body=body, order_number_type=order_number_type)

Retrieves the tracking numbers associated with the specified orders

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
api_instance = swagger_client.OrderApi(swagger_client.ApiClient(configuration))
body = ['[ \"CO0009997\", \"CO0009998\", \"CO0009999\", \"...\" ]'] # list[str] | List of order numbers base on the OrderType. (optional)
order_number_type = 56 # int | Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference) (optional)

try:
    # Retrieves the tracking numbers associated with the specified orders
    api_response = api_instance.api_order_tracking_number_post(body=body, order_number_type=order_number_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->api_order_tracking_number_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| List of order numbers base on the OrderType. | [optional] 
 **order_number_type** | **int**| Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference) | [optional] 

### Return type

[**list[OrderTracking]**](OrderTracking.md)

### Authorization

[TAPI Key](../README.md#TAPI Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

