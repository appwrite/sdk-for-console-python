from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class PlanChangeResourceCompliance(AppwriteModel):
    """
    PlanChangeResourceCompliance

    Attributes
    ----------
    type : str
        Resource type
    currentusage : float
        Current usage count
    limit : float
        Allowed limit in target plan
    status : str
        Compliance status. Either `over_limit` or `within_limit`.
    excess : float
        Number of resources exceeding the limit
    resolutionhint : str
        Suggestion for resolving the compliance issue. Empty when the resource is within limits.
    """
    type: str = Field(..., alias='type')
    currentusage: float = Field(..., alias='currentUsage')
    limit: float = Field(..., alias='limit')
    status: str = Field(..., alias='status')
    excess: float = Field(..., alias='excess')
    resolutionhint: str = Field(..., alias='resolutionHint')
