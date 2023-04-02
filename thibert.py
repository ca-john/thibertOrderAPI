from __future__ import absolute_import

import copy
import csv
import mimetypes
import certifi
import io
import json
import logging
import multiprocessing
import os
import pprint
import re
import sys
import ssl
import tempfile
import datetime
from multiprocessing.pool import ThreadPool
from typing import Any, Dict, List, Callable, Optional
import requests
import six
import urllib3
from urllib.parse import urlencode
from six.moves import http_client as httplib
from six.moves.urllib.parse import quote
#import swagger_client

import cred
import models

HOST: str = cred.HOST
KEY: str = cred.KEY
JSON_URL: str = cred.JSON_URL
LOG_FILE: str = "order_log.csv"
TIMEOUT = 500    # seconds

ENDPOINT_DICT: Dict = {
    "order":
        "/api/Order",
    "tracking_number":
        "/api/Order/TrackingNumber",
    "order_status":
        "/api/Order/OrderStatus",
    "invoices":
        "/api/Order/Invoices",
    "invoice_pdf":
        "/api/Order/InvoicePDF",
    "vehicle_parts":
        "/api/FitmentThibert/VehicleParts/{SearchType}/{VehicleYear}/{VehicleMake}/{VehicleModel}"    # noqa
}
logger = logging.getLogger(__name__)


class TypeWithDefault(type):
    """Metaclass for creating a singleton class with a default instance."""

    def __init__(cls, name, bases, dct):
        """Run the constructor.

        Args:
            name (_type_): name of the class
            bases (_type_): base classes
            dct (_type_): dictionary of attributes
        """
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        """Return the default instance.

        Returns:
            _type_: default instance
        """
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        """Set default instance.

        Args:
            default (_type_): default instance
        """
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """Do not edit the class manually."""

    def __init__(self):
        """Initialize the constructor."""
        # Default Base url
        self.host = "/"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # function to refresh API key if expired
        self.refresh_api_key_hook: Callable = None
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""
        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("swagger_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """Set the logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status.

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status.

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """Set the logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Get API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self)

        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return f"{prefix} {key}"
            else:
                return key

    def get_basic_auth_token(self):
        """Get HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(basic_auth=self.username + ':' +
                                         self.password).get('authorization')

    def auth_settings(self):
        """Get Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'TAPI Key': {
                'type': 'api_key',
                'in': 'header',
                'key': 'x-api-key',
                'value': self.get_api_key_with_prefix('x-api-key')
            },
        }

    def to_debug_report(self):
        """Get the essential information for debugging.

        :return: The report for debugging.
        """
        return f"""Python SDK Debug Report:\n OS: {sys.platform}\n Python Version: {sys.version}\n Version of the API: V1 DEVELOPMENT\n SDK Package Version: 1.0.0."""    # noqa: E501


class RESTResponse(io.IOBase):
    """RESTResponse wraps the urllib3 HTTPResponse object."""

    def __init__(self, resp):
        """Initialize the constructor for the RESTResponse class.

        Args:
            resp (_type_): Response object from urllib3.
        """
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Return a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Return a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):
    """The RESTClientObject for OpenAPI client library builds on urllib3."""

    def __init__(self,
                 configuration: Configuration,
                 pools_size=4,
                 maxsize=None):
        """Initialize the constructor for the RESTClientObject class.

        Args:
            configuration (Configuration): Configuration object for the client.
            pools_size (int, optional): The pool size. Defaults to 4.
            maxsize (_type_, optional): Max size. Defaults to None.
        """
        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args[
                'assert_hostname'] = configuration.assert_hostname    # noqa: E501

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                **addition_pool_args)
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args)

    def request(self,
                method,
                url,
                query_params=None,
                headers=None,
                body=None,
                post_params=None,
                _preload_content=True,
                _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in [
            'GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS'
        ]

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter.")

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int,)):    # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple)
                  and len(_request_timeout) == 2):
                timeout = urllib3.Timeout(connect=_request_timeout[0],
                                          read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = '{}'
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method,
                        url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers[
                        'Content-Type'] == 'application/x-www-form-urlencoded':    # noqa: E501
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(
                        method,
                        url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method,
                                              url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = f"{type(e).__name__}\n{str(e)}"
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self,
            url,
            headers=None,
            query_params=None,
            _preload_content=True,
            _request_timeout=None):
        """Send GET request.

        Args:
            url (_type_): The URL to send the request to.
            headers (_type_, optional): Headers to include in the call.
                                        Defaults to None.
            query_params (_type_, optional): Query parameters for the call.
                                            Defaults to None.
            _preload_content (bool, optional): The preload content.
                                                Defaults to True.
            _request_timeout (_type_, optional): Timeout for the request.
                                                Defaults to None.

        Returns:
            _type_: The response from the REST call.
        """
        return self.request("GET",
                            url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self,
             url,
             headers=None,
             query_params=None,
             _preload_content=True,
             _request_timeout=None):
        """Send a HEAD request.

        Args:
            url (_type_): The base URL to send the request to.
            headers (_type_, optional): Headers to include. Defaults to None.
            query_params (_type_, optional): Query parameters to include.
                                                Defaults to None.
            _preload_content (bool, optional): The preload content.
                                                Defaults to True.
            _request_timeout (_type_, optional): Request timeout for the call.
                                                Defaults to None.

        Returns:
            _type_: The response from the REST call.
        """
        return self.request("HEAD",
                            url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self,
                url,
                headers=None,
                query_params=None,
                post_params=None,
                body=None,
                _preload_content: bool = True,
                _request_timeout: Optional[int] = None) -> None:
        """Send an OPTIONS request.

        Args:
            url (_type_): The base URL to send the request to.
            headers (_type_, optional): Headers to include. Defaults to None.
            query_params (_type_, optional): Query parameters to include.
                                                Defaults to None.
            _preload_content (bool, optional): The preload content.
                                                Defaults to True.
            _request_timeout (_type_, optional): Request timeout for the call.
                                                Defaults to None.

        Returns:
            _type_: The response from the REST call.
        """
        return self.request("OPTIONS",
                            url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self,
               url,
               headers=None,
               query_params=None,
               body=None,
               _preload_content=True,
               _request_timeout=None):
        return self.request("DELETE",
                            url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self,
             url,
             headers=None,
             query_params=None,
             post_params=None,
             body=None,
             _preload_content=True,
             _request_timeout=None):
        return self.request("POST",
                            url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self,
            url,
            headers=None,
            query_params=None,
            post_params=None,
            body=None,
            _preload_content=True,
            _request_timeout=None):
        """Send a PUT request.

        Args:
            url (_type_): The full URL to request, including scheme and
            headers (_type_, optional): Headers to include. Defaults to None.
            query_params (_type_, optional): Query parameters for the call.
                                            Defaults to None.
            post_params (_type_, optional): Post parameters for the call.
                                            Defaults to None.
            body (_type_, optional): Body of the call. Defaults to None.
            _preload_content (bool, optional): The preload content.
                                                Defaults to True.
            _request_timeout (_type_, optional): Request timeout.
                                                Defaults to None.

        Returns:
            _type_: The response.
        """
        return self.request("PUT",
                            url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self,
              url,
              headers=None,
              query_params=None,
              post_params=None,
              body=None,
              _preload_content=True,
              _request_timeout=None):
        """Send PATCH method for client API call.

        Args:
            url (_type_): The full URL to make the request to.
            headers (_type_, optional): Headers to include. Defaults to None.
            query_params (_type_, optional): Query parameters for the all.
                                            Defaults to None.
            post_params (_type_, optional): Post parameters for the call.
                                            Defaults to None.
            body (_type_, optional): Body of the call. Defaults to None.
            _preload_content (bool, optional): Preload content.
                                                Defaults to True.
            _request_timeout (_type_, optional): Timeout duration.
                                                Defaults to None.

        Returns:
            _type_: The response from the API call.
        """
        return self.request("PATCH",
                            url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):
    """Generic API exception."""

    def __init__(self, status=None, reason=None, http_resp=None):
        """Initialize the constructor.

        Args:
            status (_type_, optional): Status of the exception.
                                        Defaults to None.
            reason (_type_, optional): Reason of exit. Defaults to None.
            http_resp (_type_, optional): HTTP response code. Defaults to None.
        """
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Print custom error messages for exception."""
        error_message = f"({self.status})\n Reason: {self.reason}\n"
        if self.headers:
            error_message += "HTTP response headers: {self.headers}\n"

        if self.body:
            error_message += "HTTP response body: {self.body}\n"

        return error_message


class ApiClient(object):
    """Generic API client.

    DO NOT EDIT THIS CLASS

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int,    # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self,
                 configuration=None,
                 header_name=None,
                 header_value=None,
                 cookie=None):
        """Initialize the ApiClient.

        Args:
            configuration (_type_, optional): Configuration for the API.
                                                Defaults to None.
            header_name (_type_, optional): Header names. Defaults to None.
            header_value (_type_, optional): Header values. Defaults to None.
            cookie (_type_, optional): Cookie to use. Defaults to None.
        """
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration

        self.pool = ThreadPool()
        self.rest_client = RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'Swagger-Codegen/1.0.0/python'

    def __del__(self):
        self.pool.close()
        self.pool.join()

    @property
    def user_agent(self):
        """User agent for this API client."""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(self,
                   resource_path,
                   method,
                   path_params=None,
                   query_params=None,
                   header_params=None,
                   body=None,
                   post_params=None,
                   files=None,
                   response_type=None,
                   auth_settings=None,
                   _return_http_data_only=None,
                   collection_formats=None,
                   _preload_content=True,
                   _request_timeout=None):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = self.configuration.host + resource_path

        # perform request and return response
        response_data = self.request(method,
                                     url,
                                     query_params=query_params,
                                     headers=header_params,
                                     post_params=post_params,
                                     body=body,
                                     _preload_content=_preload_content,
                                     _request_timeout=_request_timeout)

        self.last_response = response_data

        return_data = response_data
        if _preload_content:
            # deserialize response data
            if response_type:
                return_data = self.deserialize(response_data, response_type)
            else:
                return_data = None

        if _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        """Build a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            ]
        elif isinstance(obj, tuple):
            return tuple(
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {
                obj.attribute_map[attr]: getattr(obj, attr)
                for attr, _ in six.iteritems(obj.swagger_types)
                if getattr(obj, attr) is not None
            }

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in six.iteritems(obj_dict)
        }

    def deserialize(self, response, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [
                    self.__deserialize(sub_data, sub_kls) for sub_data in data
                ]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {
                    k: self.__deserialize(v, sub_kls)
                    for k, v in six.iteritems(data)
                }

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self,
                 resource_path,
                 method,
                 path_params=None,
                 query_params=None,
                 header_params=None,
                 body=None,
                 post_params=None,
                 files=None,
                 response_type=None,
                 auth_settings=None,
                 async_req=None,
                 _return_http_data_only=None,
                 collection_formats=None,
                 _preload_content=True,
                 _request_timeout=None):
        """Make the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method, path_params,
                                   query_params, header_params, body,
                                   post_params, files, response_type,
                                   auth_settings, _return_http_data_only,
                                   collection_formats, _preload_content,
                                   _request_timeout)
        else:
            thread = self.pool.apply_async(
                self.__call_api,
                (resource_path, method, path_params, query_params,
                 header_params, body, post_params, files, response_type,
                 auth_settings, _return_http_data_only, collection_formats,
                 _preload_content, _request_timeout))
        return thread

    def request(self,
                method,
                url,
                query_params=None,
                headers=None,
                post_params=None,
                body=None,
                _preload_content=True,
                _request_timeout=None):
        """Make the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ValueError("http method must be `GET`, `HEAD`, `OPTIONS`,"
                             " `POST`, `PATCH`, `PUT` or `DELETE`.")

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(
                params, dict) else params:    # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:    # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def prepare_post_parameters(self, post_params=None, files=None):
        """Build form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in six.iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (mimetypes.guess_type(filename)[0]
                                    or 'application/octet-stream')
                        params.append(
                            tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Return `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Return `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """Update header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ValueError(
                        'Authentication token must be in `query` or `header`')

    def __deserialize_file(self, response):
        """Deserialize body to file.

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                                 content_disposition).group(1)
            path = os.path.join(os.path.dirname(path), filename)
            response_data = response.data
            with open(path, "wb") as f:
                if isinstance(response_data, str):
                    # change str to bytes so we can write it
                    response_data = response_data.encode('utf-8')
                    f.write(response_data)
                else:
                    f.write(response_data)
        return path

    def __deserialize_primitive(self, data, klass):
        """Deserialize string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserialize string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string))

    def __deserialize_datatime(self, string):
        """Deserialize string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object".format(string)))

    def __hasattr(self, object, name):
        return name in object.__class__.__dict__

    def __deserialize_model(self, data, klass):
        """Deserialize list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """
        if not klass.swagger_types and not self.__hasattr(
                klass, 'get_real_child_model'):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and klass.attribute_map[attr] in data
                        and isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if (isinstance(instance, dict) and klass.swagger_types is not None
                and isinstance(data, dict)):
            for key, value in data.items():
                if key not in klass.swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance


class Contact(object):
    """A class to represent a contact.

    Do not edit the class manually.
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {'name': 'str', 'email': 'str', 'phone_number': 'str'}

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'phone_number': 'phoneNumber'
    }

    def __init__(self,
                 name=None,
                 email=None,
                 phone_number=None):    # noqa: E501
        """Contact - a model defined in Swagger."""
        self._name = None
        self._email = None
        self._phone_number = None
        self.discriminator = None
        self.name = name
        if email is not None:
            self.email = email
        self.phone_number = phone_number

    @property
    def name(self):
        """Get the name of this Contact.

        :return: The name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this Contact.

        :param name: The name of this Contact.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`")    # noqa: E501
        self._name = name

    @property
    def email(self):
        """Get the email of this Contact.

        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Set the email of this Contact.

        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """
        self._email = email

    @property
    def phone_number(self):
        """Get the phone_number of this Contact.

        :return: The phone_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Set the phone_number of this Contact.

        :param phone_number: The phone_number of this Contact.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError(
                "Invalid value for `phone_number`, must not be `None`"
            )    # noqa: E501

        self._phone_number = phone_number

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value
        if issubclass(Contact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class Address(object):
    """Class for Address.

    Do not edit the class manually.
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        'name': 'str',
        'address1': 'str',
        'address2': 'str',
        'zip_code': 'str',
        'city': 'str',
        'state': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address1': 'address1',
        'address2': 'address2',
        'zip_code': 'zipCode',
        'city': 'city',
        'state': 'state',
        'country_code': 'countryCode'
    }

    def __init__(self,
                 name=None,
                 address1=None,
                 address2=None,
                 zip_code=None,
                 city=None,
                 state=None,
                 country_code=None):    # noqa: E501
        """Address - a model defined in Swagger."""
        self._name = None
        self._address1 = None
        self._address2 = None
        self._zip_code = None
        self._city = None
        self._state = None
        self._country_code = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country_code is not None:
            self.country_code = country_code

    @property
    def name(self):
        """Get the name of this Address.

        Name asssociated to the address.  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this Address.

        Name asssociated to the address.  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def address1(self):
        """Get the address1 of this Address.

        Number and street name combination.  # noqa: E501

        :return: The address1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Set the address1 of this Address.

        Number and street name combination.  # noqa: E501

        :param address1: The address1 of this Address.  # noqa: E501
        :type: str
        """
        self._address1 = address1

    @property
    def address2(self):
        """Get the address2 of this Address.

        Alternative number and street name combination.  # noqa: E501

        :return: The address2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Set the address2 of this Address.

        Alternative number and street name combination.  # noqa: E501

        :param address2: The address2 of this Address.  # noqa: E501
        :type: str
        """
        self._address2 = address2

    @property
    def zip_code(self):
        """Get the zip_code of this Address.

        AKA Postal code  # noqa: E501

        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Set the zip_code of this Address.

        AKA Postal code  # noqa: E501

        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type: str
        """
        self._zip_code = zip_code

    @property
    def city(self):
        """Get the city of this Address.

        Town associated with the address.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Set the city of this Address.

        Town associated with the address.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """Get the state of this Address.

        State or province depending on the country.  # noqa: E501

        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Set the state of this Address.

        State or province depending on the country.  # noqa: E501

        :param state: The state of this Address.  # noqa: E501
        :type: str
        """
        self._state = state

    @property
    def country_code(self):
        """Get the country_code of this Address.

        CA or USA  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Set the country_code of this Address.

        CA or USA  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        self._country_code = country_code

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value
        if issubclass(Address, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class OrderLine(object):
    """Class for order lines.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {"thibert_part_number": "str", "quantity": "int"}

    attribute_map = {
        "thibert_part_number": "thibertPartNumber",
        "quantity": "quantity"
    }

    def __init__(self,
                 thibert_part_number=None,
                 quantity=None):    # noqa: E501
        """Orderline - a model defined in Swagger."""
        self._thibert_part_number = None
        self._quantity = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if quantity is not None:
            self.quantity = quantity

    @property
    def thibert_part_number(self):
        """Get the thibert_part_number of this OrderLine.

        Part number in the Thibert database.  # noqa: E501

        :return: The thibert_part_number of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Set the thibert_part_number of this OrderLine.

        Part number in the Thibert database.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this OrderLine.  # noqa: E501
        :type: str
        """
        self._thibert_part_number = thibert_part_number

    @property
    def quantity(self):
        """Get the quantity of this OrderLine.

        Quantity to ship.  # noqa: E501

        :return: The quantity of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Set the quantity of this OrderLine.

        Quantity to ship.  # noqa: E501

        :param quantity: The quantity of this OrderLine.  # noqa: E501
        :type: int
        """
        self._quantity = quantity

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    ))
            else:
                result[attr] = value
        if issubclass(OrderLine, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, OrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class Order(object):
    """Class for an order.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "order_reference_number": "str",
        "shipping_address": "Address",
        "contact_info": "Contact",
        "order_lines": "list[OrderLine]",
    }

    attribute_map = {
        "order_reference_number": "orderReferenceNumber",
        "shipping_address": "shippingAddress",
        "contact_info": "contactInfo",
        "order_lines": "orderLines",
    }

    def __init__(
        self,
        order_reference_number=None,
        shipping_address=None,
        contact_info=None,
        order_lines=None,
    ):    # noqa: E501
        """Order - a model defined in Swagger."""
        self._order_reference_number = None
        self._shipping_address = None
        self._contact_info = None
        self._order_lines = None
        self.discriminator = None
        if order_reference_number is not None:
            self.order_reference_number = order_reference_number
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if contact_info is not None:
            self.contact_info = contact_info
        if order_lines is not None:
            self.order_lines = order_lines

    @property
    def order_reference_number(self):
        """Get the order_reference_number of this Order.

        User inputed for personnal reference.  # noqa: E501

        :return: The order_reference_number of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_reference_number

    @order_reference_number.setter
    def order_reference_number(self, order_reference_number):
        """Set the order_reference_number of this Order.

        User inputed for personnal reference.  # noqa: E501

        :param order_reference_number: The order_reference_number of this Order.  # noqa: E501
        :type: str
        """
        self._order_reference_number = order_reference_number

    @property
    def shipping_address(self):
        """Get the shipping_address of this Order.

        :return: The shipping_address of this Order.  # noqa: E501
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Set the shipping_address of this Order.

        :param shipping_address: The shipping_address of this Order.  # noqa: E501
        :type: Address
        """
        self._shipping_address = shipping_address

    @property
    def contact_info(self):
        """Get the contact_info of this Order.

        :return: The contact_info of this Order.  # noqa: E501
        :rtype: Contact
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Set the contact_info of this Order.

        :param contact_info: The contact_info of this Order.
        :type: Contact
        """
        self._contact_info = contact_info

    @property
    def order_lines(self):
        """Gets the order_lines of this Order.

        Parts in the order.  # noqa: E501

        :return: The order_lines of this Order.  # noqa: E501
        :rtype: list[OrderLine]
        """
        return self._order_lines

    @order_lines.setter
    def order_lines(self, order_lines):
        """Set the order_lines of this Order.

        Parts in the order.  # noqa: E501
        :param order_lines: The order_lines of this Order.  # noqa: E501
        :type: list[OrderLine]
        """
        self._order_lines = order_lines

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    ))
            else:
                result[attr] = value
        if issubclass(Order, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other


class APIConnector:
    """A base class for connecting to an API."""

    def __init__(self,
                 base_url: str = HOST,
                 api_key: str = KEY,
                 authorization: str = KEY):
        """Initialize the API connector.

        Args:
            base_url (str): Base URL for the API.
            api_key (str): The API key.
            authorization (str): Authorization header.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.authorization = authorization
        self.base_url = base_url

    def get_data(self, endpoint: str, params=None) -> Any:
        """Get data from the API.

        Args:
            endpoint (str): The url endpoint.
            params (Any, optional): Parameters to the endpoint.
                                    Defaults to None.

        Returns:
            Any: The response data.
        """
        url = self.base_url + endpoint
        headers = {
            "x-api-key": self.api_key,
            "Authorization": self.authorization
        }
        response = requests.get(url,
                                params=params,
                                headers=headers,
                                timeout=TIMEOUT)
        return response.json()

    def post_data(self, endpoint: str, data: Dict) -> Any:
        """Post data to the API.

        Args:
            endpoint (str): The endpoint.
            data (Dict): Data to be posted.

        Returns:
            Any: The response data.
        """
        url = self.base_url + endpoint
        headers = {
            "x-api-key": self.api_key,
            "Authorization": self.authorization,
            "Content-Type": "application/json"
        }
        response = requests.post(url,
                                 json=data,
                                 headers=headers,
                                 timeout=TIMEOUT)
        return response.json()


class OrderApi(object):
    """DO NOT EDIT THIS CLASS."""

    def __init__(self, api_client: ApiClient = None):
        """Initialize a new OrderApi with given client.

        Args:
            api_client (ApiClient, optional): The API Client to use.
                                            Defaults to None.
        """
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_order_invoice_pdf_get(self, **kwargs):    # noqa: E501
        """Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller's side.  # noqa.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoice_pdf_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: Invoice number
        :param str original_order_id: Order number of the specified invoice
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_invoice_pdf_get_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_invoice_pdf_get_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_invoice_pdf_get_with_http_info(self,
                                                 **kwargs):    # noqa: E501
        """Download a base64 string representation of an invoice PDF. The response must be parsed into a PDF on the caller's side.  # noqa.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoice_pdf_get_with_http_info(async_req=True) # noqa
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: Invoice number
        :param str original_order_id: Order number related to the specified invoice # noqa
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['invoice_id', 'original_order_id']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_invoice_pdf_get")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'invoice_id' in params:
            query_params.append(
                ('invoiceId', params['invoice_id']))    # noqa: E501
        if 'original_order_id' in params:
            query_params.append(('originalOrderId',
                                 params['original_order_id']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/InvoicePDF',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_invoices_get(self, **kwargs):    # noqa: E501
        """Retrieve invoices associated to the account in pages of 10.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoices_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start_date: Filter invoices by start date
        :param datetime end_date: Filter invoices by end date
        :param int page: Page to retrieve
        :return: list[Invoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_invoices_get_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_invoices_get_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_invoices_get_with_http_info(self, **kwargs):    # noqa: E501
        """Retrieve invoices associated to the account in pages of 10.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_invoices_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start_date: Filter invoices by start date
        :param datetime end_date: Filter invoices by end date
        :param int page: Page to retrieve
        :return: list[Invoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['start_date', 'end_date', 'page']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_invoices_get")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(
                ('startDate', params['start_date']))    # noqa: E501
        if 'end_date' in params:
            query_params.append(
                ('endDate', params['end_date']))    # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/Invoices',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Invoice]',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_order_status_post(self, **kwargs):    # noqa: E501
        """Retrieve the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_order_status_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)  # noqa
        :param int page_number: Number of the page to retrieve. Default value: 1
        :param int page_size: Number of results per page. Default value: 50, Maximum allowed: 200
        :return: list[OrderStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_order_status_post_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_order_status_post_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_order_status_post_with_http_info(self,
                                                   **kwargs):    # noqa: E501
        """Retrieve the order status associated with the specified order numbers. If there is no order number specified, all orders will be returned.  # noqa.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_order_status_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)
        :param int page_number: Number of the page to retrieve. Default value: 1
        :param int page_size: Number of results per page. Default value: 50, Maximum allowed: 200
        :return: list[OrderStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['body', 'order_number_type', 'page_number',
                      'page_size']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_order_status_post")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number_type' in params:
            query_params.append(('OrderNumberType',
                                 params['order_number_type']))    # noqa: E501
        if 'page_number' in params:
            query_params.append(
                ('PageNumber', params['page_number']))    # noqa: E501
        if 'page_size' in params:
            query_params.append(
                ('PageSize', params['page_size']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(    # noqa: E501
                ['application/json', 'text/json',
                 'application/*+json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/OrderStatus',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OrderStatus]',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_post(self, **kwargs):    # noqa: E501
        """Process an order in our systems.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Order body: Order to be saved.
        :return: OrderConfirmation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_post_with_http_info(**kwargs)    # noqa: E501
        (data) = self.api_order_post_with_http_info(**kwargs)    # noqa: E501
        return data

    def api_order_post_with_http_info(self, **kwargs):    # noqa: E501
        """Process an order in our systems.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Order body: Order to be saved.
        :return: OrderConfirmation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['body']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_post")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(    # noqa: E501
                ['application/json', 'text/json',
                 'application/*+json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderConfirmation',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_order_tracking_number_post(self, **kwargs):    # noqa: E501
        """Retrieve the tracking numbers associated with the specified orders.  # noqa.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_tracking_number_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType.
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)
        :return: list[OrderTracking]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_order_tracking_number_post_with_http_info(
                **kwargs)    # noqa: E501
        else:
            (data) = self.api_order_tracking_number_post_with_http_info(
                **kwargs)    # noqa: E501
            return data

    def api_order_tracking_number_post_with_http_info(
            self, **kwargs):    # noqa: E501
        """Retrieve the tracking numbers associated with the specified orders.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_order_tracking_number_post_with_http_info(async_req=True)  # noqa
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: List of order numbers base on the OrderType.
        :param int order_number_type: Type of order number used for the search. Values: 1 (ThibertOrderNumber), 2 (OrderReferenceNumber/WebOrderReference)  # noqa
        :return: list[OrderTracking]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = ['body', 'order_number_type']    # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}"
                                " to method api_order_tracking_number_post")
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_number_type' in params:
            query_params.append(('OrderNumberType',
                                 params['order_number_type']))    # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])    # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(    # noqa: E501
                ['application/json', 'text/json',
                 'application/*+json'])    # noqa: E501

        # Authentication setting
        auth_settings = ['TAPI Key']    # noqa: E501

        return self.api_client.call_api(
            '/api/Order/TrackingNumber',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OrderTracking]',    # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


def get_paths(url: str = JSON_URL) -> Dict[str, Dict]:
    """Get the paths from the OpenAPI JSON file.

    Args:
        url (str, optional): The url to the JSON specification file.
                            Defaults to JSON_URL.

    Returns:
        Dict[str, Dict]: Return the paths from the JSON file.
    """
    response = requests.get(url, timeout=500).text
    response_info = json.loads(response)
    print(f"Connected to OpenAPI ver {response_info.get('openapi')}")
    if response_info.get("paths") is None:
        print("No paths found.")
    return response_info.get("paths")


def write_order_log(order_number: str,
                    order_date: str,
                    filename: str = LOG_FILE) -> None:
    """Write order the log to the log file, if it exists. Create the file if it does not.  # noqa.

    Args:
        filename (str, optional): The file name of the log file. Defaults to LOG_FILE.
        order_number (str): The order number.
        order_date (str): The order date.
    """
    # Check if the file exists and create if it doesn't, including the header
    header = ["Log time", "Order Creation Date", "Order Number"]
    if not os.path.exists(filename):
        # Create the file
        with open(filename, "a+", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
        file.close()

    # Write the data to the file
    with open(filename, "a+", encoding="utf-8") as file:
        writer = csv.writer(file)
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
        row = [timestamp, order_date, order_number]
        writer.writerow(row)

    # Close the file
    file.close()


def main():
    """Start the main entry point of the app.

    This is where we get the input from the user and
    create the order and submit it.
    """
    # api = CarLightingDistrictAPI()

    # # Example usage
    # years = api.get_vehicle_years()
    # print("Years:", years)

    # Check the paths
    paths = get_paths()
    assert paths is not None
    assert len(paths) > 0

    # if years:
    #     makes = api.get_vehicle_makes(years[0])
    #     print("Makes for the first year:", makes)

    #     if makes:
    #         models = api.get_vehicle_models(years[0], makes[0])
    #         print(f"Models for {years[0]} and {makes[0]}:", models)
    # write_order_log("123456", "2021-01-01")

    print("Thibert Order API\n")

    ref_number: str = input("Enter the order reference number: ")
    customer_name: str = input("Enter the customer name: ")
    customer_shipping_address1: str = input("Enter shipping address1: ")
    customer_shipping_address2: str = input(
        "Enter shipping address2, press enter if empty: ")
    customer_zip_code: str = input("Enter the zip code: ")
    customer_city: str = input("Enter the city: ")
    customer_state: str = input("Enter the state: ")
    country_code: str = input("Enter the country code: ")

    contact_name: str = input("Enter the contact name: ")
    contact_email: str = input("Enter the contact email: ")
    contact_phone_number: str = input("Enter the contact phone number: ")

    order_lines: List[OrderLine] = []
    print("Order Line - Enter the part number and quantity for each part:")
    print(" ")
    while True:
        part_number = input("Enter the part number: ")
        quantity = input("Enter the quantity: ")
        if not (part_number and quantity):
            print("Part number and quantity are required.")
            continue
        if not quantity.isdigit():
            print("Quantity must be a number.")
            continue
        # order_lines.append({
        #     "thibertPartNumber": part_number,
        #     "quantity": int(quantity)
        # })

        line_item = OrderLine()
        line_item.thibert_part_number = part_number
        line_item.quantity = int(quantity)
        order_lines.append(line_item)

        if input("Add another part? (y/n): ") == "n":
            break

    # Contact for the order
    contact = Contact(name=contact_name,
                      email=contact_email,
                      phone_number=contact_phone_number)
    # contact.name = contact_name
    # contact.email = contact_email
    # contact.phone_number = contact_phone_number

    # Customer for the order
    customer_address = Address(name=customer_name,
                               address1=customer_shipping_address1,
                               address2=customer_shipping_address2,
                               zip_code=customer_zip_code,
                               city=customer_city,
                               state=customer_state,
                               country_code=country_code)
    # customer_address.name = customer_name
    # customer_address.address1 = customer_shipping_address1
    # customer_address.address2 = customer_shipping_address2
    # customer_address.zip_code = customer_zip_code
    # customer_address.city = customer_city
    # customer_address.state = customer_state
    # customer_address.country_code = country_code
    order_obj = Order(order_reference_number=ref_number,
                      contact_info=contact,
                      shipping_address=customer_address,
                      order_lines=order_lines)
    # order_obj.order_reference_number = ref_number
    # order_obj.contact_info = contact
    # order_obj.shipping_address = customer_address

    order_api = OrderApi()

    # order.order(order_obj)

    print(order_obj.to_str())
    print(
        "---CONFIRM THAT THE INFORMATION IS CORRECT BEFORE SUBMITTING THE ORDER.---"    # noqa
    )

    if input("Submit the order? (y/n): ") == "y":
        print("Submitting the order...")
        res = order_api.api_order_post(order_obj)
        print(f"The result of the call is: {res}")
    else:
        print("Cancelled - Order not submitted.")


if __name__ == "__main__":
    main()
