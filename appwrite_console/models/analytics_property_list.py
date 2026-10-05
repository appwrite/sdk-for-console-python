from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .analytics_property import AnalyticsProperty


class AnalyticsPropertyList(AppwriteModel):
    """
    Analytics properties list

    Attributes
    ----------
    total : float
        Total number of properties that matched your query.
    properties : List[AnalyticsProperty]
        List of properties.
    """

    total: float = Field(..., alias='total')
    properties: List[AnalyticsProperty] = Field(..., alias='properties')
