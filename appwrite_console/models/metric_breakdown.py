from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class MetricBreakdown(AppwriteModel):
    """
    Metric Breakdown

    Attributes
    ----------
    resourceid : Optional[str]
        Resource ID.
    name : str
        Resource name.
    value : float
        The value of this metric at the timestamp.
    estimate : Optional[float]
        The estimated value of this metric at the end of the period.
    """

    resourceid: Optional[str] = Field(default=None, alias='resourceId')
    name: str = Field(..., alias='name')
    value: float = Field(..., alias='value')
    estimate: Optional[float] = Field(default=None, alias='estimate')
