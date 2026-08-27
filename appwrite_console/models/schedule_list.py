from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .schedule import Schedule


class ScheduleList(AppwriteModel):
    """
    Schedules List

    Attributes
    ----------
    total : float
        Total number of schedules that matched your query.
    schedules : List[Schedule]
        List of schedules.
    """

    total: float = Field(..., alias='total')
    schedules: List[Schedule] = Field(..., alias='schedules')
