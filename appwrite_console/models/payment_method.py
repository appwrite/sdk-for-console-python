from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class PaymentMethod(AppwriteModel):
    """
    paymentMethod

    Attributes
    ----------
    id : str
        Payment Method ID.
    createdat : str
        Payment method creation time in ISO 8601 format.
    updatedat : str
        Payment method update date in ISO 8601 format.
    permissions : List[Any]
        Payment method permissions. [Learn more about permissions](/docs/permissions).
    providermethodid : str
        Payment method ID from the payment provider
    clientsecret : str
        Client secret hash for payment setup
    provideruserid : str
        User ID from the payment provider.
    userid : str
        ID of the Team.
    expirymonth : float
        Expiry month of the payment method.
    expiryyear : float
        Expiry year of the payment method.
    last4 : str
        Last 4 digit of the payment method
    brand : str
        Payment method brand
    name : str
        Name of the owner
    mandateid : str
        Mandate ID of the payment method
    country : str
        Country of the payment method
    state : str
        State of the payment method
    lasterror : str
        Last payment error associated with the payment method.
    default : bool
        True when it&#039;s the default payment method.
    expired : bool
        True when payment method has expired.
    failed : bool
        True when payment method has failed to process multiple times.
    """

    id: str = Field(
        ...,
        alias='$id',
    )
    createdat: str = Field(
        ...,
        alias='$createdAt',
    )
    updatedat: str = Field(
        ...,
        alias='$updatedAt',
    )
    permissions: List[Any] = Field(
        ...,
        alias='$permissions',
    )
    providermethodid: str = Field(
        ...,
        alias='providerMethodId',
    )
    clientsecret: str = Field(
        ...,
        alias='clientSecret',
    )
    provideruserid: str = Field(
        ...,
        alias='providerUserId',
    )
    userid: str = Field(
        ...,
        alias='userId',
    )
    expirymonth: float = Field(
        ...,
        alias='expiryMonth',
    )
    expiryyear: float = Field(
        ...,
        alias='expiryYear',
    )
    last4: str = Field(
        ...,
        alias='last4',
    )
    brand: str = Field(
        ...,
        alias='brand',
    )
    name: str = Field(
        ...,
        alias='name',
    )
    mandateid: str = Field(
        ...,
        alias='mandateId',
    )
    country: str = Field(
        ...,
        alias='country',
    )
    state: str = Field(
        ...,
        alias='state',
    )
    lasterror: str = Field(
        ...,
        alias='lastError',
    )
    default: bool = Field(
        ...,
        alias='default',
    )
    expired: bool = Field(
        ...,
        alias='expired',
    )
    failed: bool = Field(
        ...,
        alias='failed',
    )
