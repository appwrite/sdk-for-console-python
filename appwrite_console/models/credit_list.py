from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .credit import Credit

class CreditList(AppwriteModel):
    """
    CreditList

    Attributes
    ----------
    credits : List[Credit]
        Credits
    total : float
        Total number of credits
    available : float
        Total available credit balance in USD
    """
    credits: List[Credit] = Field(..., alias='credits')
    total: float = Field(..., alias='total')
    available: float = Field(..., alias='available')
