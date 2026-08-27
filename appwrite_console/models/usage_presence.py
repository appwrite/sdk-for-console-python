from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .metric import Metric


class UsagePresence(AppwriteModel):
    """
    UsagePresence

    Attributes
    ----------
    range : str
        Time range of the usage stats.
    usersonlinetotal : float
        Current total number of online users.
    presences : List[Metric]
        Aggregated number of online users per period.
    """

    range: str = Field(..., alias='range')
    usersonlinetotal: float = Field(..., alias='usersOnlineTotal')
    presences: List[Metric] = Field(..., alias='presences')
