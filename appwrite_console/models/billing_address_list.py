from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .billing_address import BillingAddress

class BillingAddressList(AppwriteModel):
    """
    Billing address list

    Attributes
    ----------
    total : float
        Total number of billingAddresses that matched your query.
    billingaddresses : List[BillingAddress]
        List of billingAddresses.
    """
    total: float = Field(..., alias='total')
    billingaddresses: List[BillingAddress] = Field(..., alias='billingAddresses')
