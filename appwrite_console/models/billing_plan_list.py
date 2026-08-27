from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .billing_plan import BillingPlan


class BillingPlanList(AppwriteModel):
    """
    Billing plan list

    Attributes
    ----------
    total : float
        Total number of plans that matched your query.
    plans : List[BillingPlan]
        List of plans.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    plans: List[BillingPlan] = Field(
        ...,
        alias='plans',
    )
