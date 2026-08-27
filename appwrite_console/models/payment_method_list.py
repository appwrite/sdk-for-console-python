from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .payment_method import PaymentMethod


class PaymentMethodList(AppwriteModel):
    """
    Payment methods list

    Attributes
    ----------
    total : float
        Total number of paymentMethods that matched your query.
    paymentmethods : List[PaymentMethod]
        List of paymentMethods.
    """

    total: float = Field(..., alias='total')
    paymentmethods: List[PaymentMethod] = Field(..., alias='paymentMethods')
