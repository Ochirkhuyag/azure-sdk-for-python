# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ErrorResponseBody(Model):
    """Error response indicates that the service is not able to process the
    incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~azure.mgmt.subscription.models.ErrorResponse
    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, error=None, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.error = error
        self.code = code
        self.message = message


class ErrorResponseBodyException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponseBody'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseBodyException, self).__init__(deserialize, response, 'ErrorResponseBody', *args)
