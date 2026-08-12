from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class Schedule(AppwriteModel):
    """
    Schedule

    Attributes
    ----------
    id : str
        Schedule ID.
    createdat : str
        Schedule creation date in ISO 8601 format.
    updatedat : str
        Schedule update date in ISO 8601 format.
    resourcetype : str
        The resource type associated with this schedule.
    resourceid : str
        The resource ID associated with this schedule.
    resourceupdatedat : str
        Change-tracking timestamp used by the scheduler to detect resource changes in ISO 8601 format.
    projectid : str
        The project ID associated with this schedule.
    schedule : str
        The CRON schedule expression.
    data : Dict[str, Any]
        Schedule data used to store resource-specific context needed for execution.
    active : bool
        Whether the schedule is active.
    region : str
        The region where the schedule is deployed.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    resourceupdatedat: str = Field(..., alias='resourceUpdatedAt')
    projectid: str = Field(..., alias='projectId')
    schedule: str = Field(..., alias='schedule')
    data: Dict[str, Any] = Field(..., alias='data')
    active: bool = Field(..., alias='active')
    region: str = Field(..., alias='region')
