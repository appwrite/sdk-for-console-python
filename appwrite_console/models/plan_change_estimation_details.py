from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class PlanChangeEstimationDetails(AppwriteModel):
    """
    PlanChangeEstimationDetails

    Attributes
    ----------
    currency : str
        Currency code
    grossamount : float
        Gross amount after all discounts and credits
    credits : float
        Credits applied from coupon
    organizationcredits : float
        Organization&#039;s existing credits applied
    discount : float
        Discount amount from prorated invoices
    amount : float
        Total amount before discounts and credits
    nextinvoicedate : str
        Next invoice date
    items : List[Any]
        Line items breakdown
    discounts : List[Any]
        Applied discounts breakdown
    """

    currency: str = Field(..., alias='currency')
    grossamount: float = Field(..., alias='grossAmount')
    credits: float = Field(..., alias='credits')
    organizationcredits: float = Field(..., alias='organizationCredits')
    discount: float = Field(..., alias='discount')
    amount: float = Field(..., alias='amount')
    nextinvoicedate: str = Field(..., alias='nextInvoiceDate')
    items: List[Any] = Field(..., alias='items')
    discounts: List[Any] = Field(..., alias='discounts')
