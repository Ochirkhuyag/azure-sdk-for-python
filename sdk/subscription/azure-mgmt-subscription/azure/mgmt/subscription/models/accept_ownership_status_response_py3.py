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


class AcceptOwnershipStatusResponse(Model):
    """Subscription Accept Ownership Response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar subscription_id: Newly created subscription Id.
    :vartype subscription_id: str
    :param accept_ownership_state: Possible values include: 'Pending',
     'Completed', 'Expired'
    :type accept_ownership_state: str or
     ~azure.mgmt.subscription.models.AcceptOwnership
    :param provisioning_state: Possible values include: 'Pending', 'Accepted',
     'Succeeded'
    :type provisioning_state: str or
     ~azure.mgmt.subscription.models.Provisioning
    :ivar billing_owner: UPN of the billing owner
    :vartype billing_owner: str
    :param subscription_tenant_id: Tenant Id of the subscription
    :type subscription_tenant_id: str
    :param display_name: The display name of the subscription.
    :type display_name: str
    :param tags: Tags for the subscription
    :type tags: dict[str, str]
    """

    _validation = {
        'subscription_id': {'readonly': True},
        'billing_owner': {'readonly': True},
    }

    _attribute_map = {
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'accept_ownership_state': {'key': 'acceptOwnershipState', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'billing_owner': {'key': 'billingOwner', 'type': 'str'},
        'subscription_tenant_id': {'key': 'subscriptionTenantId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, accept_ownership_state=None, provisioning_state=None, subscription_tenant_id: str=None, display_name: str=None, tags=None, **kwargs) -> None:
        super(AcceptOwnershipStatusResponse, self).__init__(**kwargs)
        self.subscription_id = None
        self.accept_ownership_state = accept_ownership_state
        self.provisioning_state = provisioning_state
        self.billing_owner = None
        self.subscription_tenant_id = subscription_tenant_id
        self.display_name = display_name
        self.tags = tags
