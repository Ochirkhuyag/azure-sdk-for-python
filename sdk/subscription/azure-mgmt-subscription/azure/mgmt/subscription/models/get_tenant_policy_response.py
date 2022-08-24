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


class GetTenantPolicyResponse(Model):
    """Tenant policy Information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Policy Id.
    :vartype id: str
    :ivar name: Policy name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param properties: Tenant policy properties.
    :type properties: ~azure.mgmt.subscription.models.TenantPolicy
    :ivar system_data:
    :vartype system_data: ~azure.mgmt.subscription.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'TenantPolicy'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(self, **kwargs):
        super(GetTenantPolicyResponse, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = kwargs.get('properties', None)
        self.system_data = None
