from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .analytics_metric import AnalyticsMetric


class AnalyticsMetricList(AppwriteModel):
    """
    AnalyticsMetricList

    Attributes
    ----------
    total : float
        Total number of metric rows returned.
    metrics : List[AnalyticsMetric]
        Metric rows: one per time bucket, one per dimension value, or a single row for the flat aggregate.
    """

    total: float = Field(..., alias='total')
    metrics: List[AnalyticsMetric] = Field(..., alias='metrics')
