from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AddonPrice(AppwriteModel):
    """
    AddonPrice

    Attributes
    ----------
    addonkey : str
        Addon key.
    name : str
        Addon display name.
    monthlyprice : float
        Full monthly price of the addon.
    proratedamount : float
        Calculated prorated amount for the current billing cycle.
    remainingdays : float
        Days remaining in the current billing cycle.
    totalcycledays : float
        Total days in the billing cycle.
    currency : str
        Currency code.
    billingcycleend : str
        When the current billing cycle ends.
    """
    addonkey: str = Field(..., alias='addonKey')
    name: str = Field(..., alias='name')
    monthlyprice: float = Field(..., alias='monthlyPrice')
    proratedamount: float = Field(..., alias='proratedAmount')
    remainingdays: float = Field(..., alias='remainingDays')
    totalcycledays: float = Field(..., alias='totalCycleDays')
    currency: str = Field(..., alias='currency')
    billingcycleend: str = Field(..., alias='billingCycleEnd')
