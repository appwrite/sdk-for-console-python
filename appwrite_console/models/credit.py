from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Credit(AppwriteModel):
    """
    Credit

    Attributes
    ----------
    id : str
        Credit ID.
    createdat : str
        Credit creation time in ISO 8601 format.
    updatedat : str
        Credit update date in ISO 8601 format.
    permissions : List[Any]
        Credit permissions. [Learn more about permissions](/docs/permissions).
    couponid : str
        coupon ID
    userid : str
        ID of the User.
    teamid : str
        ID of the Team.
    credits : float
        Provided credit amount
    total : float
        Provided credit amount
    expiration : str
        Credit expiration time in ISO 8601 format.
    status : str
        Status of the credit. Can be one of `disabled`, `active` or `expired`.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    couponid: str = Field(..., alias='couponId')
    userid: str = Field(..., alias='userId')
    teamid: str = Field(..., alias='teamId')
    credits: float = Field(..., alias='credits')
    total: float = Field(..., alias='total')
    expiration: str = Field(..., alias='expiration')
    status: str = Field(..., alias='status')
