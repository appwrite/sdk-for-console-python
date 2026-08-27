from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_metric import UsageMetric


class UsageEventList(AppwriteModel):
    """
    usageEventList

    Attributes
    ----------
    interval : str
        Requested interval, or an empty string for a flat aggregate.
    metrics : List[UsageMetric]
        One series per requested event metric.
    """

    interval: str = Field(
        ...,
        alias='interval',
    )
    metrics: List[UsageMetric] = Field(
        ...,
        alias='metrics',
    )
