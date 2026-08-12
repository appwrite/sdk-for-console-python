from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AffiliateReward(AppwriteModel):
    """
    AffiliateReward

    Attributes
    ----------
    id : str
        Reward ID.
    createdat : str
        Reward creation date in ISO 8601 format.
    updatedat : str
        Reward update date in ISO 8601 format.
    userid : str
        User ID of the reward owner.
    linkid : str
        Affiliate link ID that earned this reward.
    referralid : str
        Referral ID that earned this reward.
    amount : float
        Reward amount in USD.
    status : str
        Reward status. Can be one of `pending` or `claimed`.
    teamid : Optional[str]
        Organization ID the reward was claimed on.
    creditid : Optional[str]
        Credit document ID created when the reward was claimed.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    linkid: str = Field(..., alias='linkId')
    referralid: str = Field(..., alias='referralId')
    amount: float = Field(..., alias='amount')
    status: str = Field(..., alias='status')
    teamid: Optional[str] = Field(default=None, alias='teamId')
    creditid: Optional[str] = Field(default=None, alias='creditId')
