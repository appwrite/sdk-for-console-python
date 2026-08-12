from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class Addon(AppwriteModel):
    """
    Addon

    Attributes
    ----------
    id : str
        Addon ID.
    createdat : str
        Addon creation time in ISO 8601 format.
    updatedat : str
        Addon update date in ISO 8601 format.
    permissions : List[Any]
        Addon permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    key : str
        Addon key
    resourcetype : str
        Resource type (organization or project)
    resourceid : str
        Resource ID
    status : str
        Payment status. Possible values: pending (awaiting payment confirmation e.g. 3DS), active (payment confirmed and addon is running).
    currentvalue : float
        Current value for this billing cycle. For toggle addons: 1 (on) or 0 (off). For numeric addons: the active quantity.
    nextvalue : Optional[float]
        Value to apply at the start of the next billing cycle. Null means no change is scheduled. For toggle addons, 0 means the addon will be removed at the next cycle.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    key: str = Field(..., alias='key')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    status: str = Field(..., alias='status')
    currentvalue: float = Field(..., alias='currentValue')
    nextvalue: Optional[float] = Field(default=None, alias='nextValue')
