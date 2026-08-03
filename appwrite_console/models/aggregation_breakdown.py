from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_resources import UsageResources

class AggregationBreakdown(AppwriteModel):
    """
    Breakdown

    Attributes
    ----------
    id : str
        Aggregation ID.
    name : str
        Project name
    region : str
        Project region
    amount : float
        Aggregated amount
    resources : List[UsageResources]
        Typed model field.
    """
    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    region: str = Field(..., alias='region')
    amount: float = Field(..., alias='amount')
    resources: List[UsageResources] = Field(..., alias='resources')
