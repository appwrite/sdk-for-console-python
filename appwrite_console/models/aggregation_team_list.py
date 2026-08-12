from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .aggregation_team import AggregationTeam

class AggregationTeamList(AppwriteModel):
    """
    Aggregation team list

    Attributes
    ----------
    total : float
        Total number of aggregations that matched your query.
    aggregations : List[AggregationTeam]
        List of aggregations.
    """
    total: float = Field(..., alias='total')
    aggregations: List[AggregationTeam] = Field(..., alias='aggregations')
