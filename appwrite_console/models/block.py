from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class Block(AppwriteModel):
    """
    Block

    Attributes
    ----------
    createdat : str
        Block creation date in ISO 8601 format.
    resourcetype : str
        Resource type that is blocked
    resourceid : str
        Resource identifier that is blocked
    mode : str
        Block mode. full blocks reads and writes; readOnly blocks writes only.
    expiredat : Optional[str]
        Block expiration date in ISO 8601 format. Can be null if the block does not expire.
    """

    createdat: str = Field(..., alias='$createdAt')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    mode: str = Field(..., alias='mode')
    expiredat: Optional[str] = Field(default=None, alias='expiredAt')
