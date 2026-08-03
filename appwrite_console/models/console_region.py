from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ConsoleRegion(AppwriteModel):
    """
    Region

    Attributes
    ----------
    id : str
        Region ID
    name : str
        Region name
    available : bool
        Does the organization have access to this region.
    disabled : bool
        Does the backend support this region.
    default : bool
        Is this the region default.
    flag : str
        Region flag code.
    """
    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    available: bool = Field(..., alias='available')
    disabled: bool = Field(..., alias='disabled')
    default: bool = Field(..., alias='default')
    flag: str = Field(..., alias='flag')
