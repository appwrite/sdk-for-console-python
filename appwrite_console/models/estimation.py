from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .estimation_item import EstimationItem

class Estimation(AppwriteModel):
    """
    Estimation

    Attributes
    ----------
    amount : float
        Total amount
    grossamount : float
        Gross payable amount
    discount : float
        Discount amount
    credits : float
        Credits amount
    items : List[EstimationItem]
        Estimation items
    discounts : List[EstimationItem]
        Estimation discount items
    trialdays : float
        Trial days
    trialenddate : Optional[str]
        Trial end date
    """
    amount: float = Field(..., alias='amount')
    grossamount: float = Field(..., alias='grossAmount')
    discount: float = Field(..., alias='discount')
    credits: float = Field(..., alias='credits')
    items: List[EstimationItem] = Field(..., alias='items')
    discounts: List[EstimationItem] = Field(..., alias='discounts')
    trialdays: float = Field(..., alias='trialDays')
    trialenddate: Optional[str] = Field(default=None, alias='trialEndDate')
