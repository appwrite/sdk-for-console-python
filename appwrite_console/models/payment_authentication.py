from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class PaymentAuthentication(AppwriteModel):
    """
    PaymentAuthentication

    Attributes
    ----------
    message : str
        Message for the end user to show on Console.
    clientsecret : str
        Stripe client secret to use for validation.
    organizationid : str
        Organization ID for which the payment authentication is needed.
    invoiceid : str
        Invoice ID against which the payment needs to be validated.
    addonid : str
        Addon ID to use when calling the addon validate endpoint. Empty when authentication is not for an addon.
    projectid : str
        Project ID for project-level addon payments. Empty for organization-level addons.
    """

    message: str = Field(..., alias='message')
    clientsecret: str = Field(..., alias='clientSecret')
    organizationid: str = Field(..., alias='organizationId')
    invoiceid: str = Field(..., alias='invoiceId')
    addonid: str = Field(..., alias='addonId')
    projectid: str = Field(..., alias='projectId')
