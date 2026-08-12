from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AffiliateLink(AppwriteModel):
    """
    AffiliateLink

    Attributes
    ----------
    id : str
        Link ID. This is the shareable referral code.
    createdat : str
        Link creation date in ISO 8601 format.
    updatedat : str
        Link update date in ISO 8601 format.
    userid : str
        User ID of the link owner.
    name : str
        Optional link name.
    status : str
        Link status. Can be one of `active` or `disabled`.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    name: str = Field(..., alias='name')
    status: str = Field(..., alias='status')
