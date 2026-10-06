from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class BillingAddress(AppwriteModel):
    """
    Address

    Attributes
    ----------
    id : str
        Region ID
    userid : str
        User ID
    streetaddress : str
        Street address
    addressline2 : Optional[str]
        Address line 2
    country : str
        Address country
    city : str
        city
    state : Optional[str]
        state
    postalcode : Optional[str]
        postal code
    """

    id: str = Field(..., alias='$id')
    userid: str = Field(..., alias='userId')
    streetaddress: str = Field(..., alias='streetAddress')
    addressline2: Optional[str] = Field(default=None, alias='addressLine2')
    country: str = Field(..., alias='country')
    city: str = Field(..., alias='city')
    state: Optional[str] = Field(default=None, alias='state')
    postalcode: Optional[str] = Field(default=None, alias='postalCode')
