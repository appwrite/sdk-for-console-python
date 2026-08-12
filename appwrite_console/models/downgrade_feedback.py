from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DowngradeFeedback(AppwriteModel):
    """
    Downgrade Feedback

    Attributes
    ----------
    id : str
        Feedback ID.
    createdat : str
        Feedback creation date in ISO 8601 format.
    updatedat : str
        Feedback update date in ISO 8601 format.
    title : str
        Feedback reason
    message : str
        Feedback message
    fromplanid : str
        Plan ID downgrading from
    toplanid : str
        Plan ID downgrading to
    teamid : str
        Organization ID
    userid : str
        User ID who submitted feedback
    version : str
        Console version
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    title: str = Field(..., alias='title')
    message: str = Field(..., alias='message')
    fromplanid: str = Field(..., alias='fromPlanId')
    toplanid: str = Field(..., alias='toPlanId')
    teamid: str = Field(..., alias='teamId')
    userid: str = Field(..., alias='userId')
    version: str = Field(..., alias='version')
