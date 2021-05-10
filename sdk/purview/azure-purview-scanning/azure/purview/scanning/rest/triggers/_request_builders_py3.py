# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional, Union

from azure.core.pipeline.transport._base import _format_url_section
from azure.purview.scanning.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_get_trigger_request(
    data_source_name: str,
    scan_name: str,
    **kwargs: Any
) -> HttpRequest:
    """Gets trigger information.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :param scan_name:
    :type scan_name: str
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "properties": {}
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}/scans/{scanName}/triggers/default')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
        'scanName': _SERIALIZER.url("scan_name", scan_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_trigger_request(
    data_source_name: str,
    scan_name: str,
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Creates an instance of a trigger.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :param scan_name:
    :type scan_name: str
    :keyword json:
    :paramtype json: Any
    :keyword content:
    :paramtype content: Any
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # JSON input template you can fill out and use as your `json` input.
            json = {
                "properties": {}
            }


            # response body for status code(s): 200, 201
            response_body == {
                "properties": {}
            }

    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}/scans/{scanName}/triggers/default')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
        'scanName': _SERIALIZER.url("scan_name", scan_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_trigger_request(
    data_source_name: str,
    scan_name: str,
    **kwargs: Any
) -> HttpRequest:
    """Deletes the trigger associated with the scan.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your code flow.

    :param data_source_name:
    :type data_source_name: str
    :param scan_name:
    :type scan_name: str
    :return: Returns an :class:`~azure.purview.scanning.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this response into your code flow.
    :rtype: ~azure.purview.scanning.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "properties": {}
            }

    """
    api_version = "2018-12-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datasources/{dataSourceName}/scans/{scanName}/triggers/default')
    path_format_arguments = {
        'dataSourceName': _SERIALIZER.url("data_source_name", data_source_name, 'str'),
        'scanName': _SERIALIZER.url("scan_name", scan_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )
