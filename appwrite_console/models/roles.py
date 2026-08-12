from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Roles(AppwriteModel):
    """
    Roles

    Attributes
    ----------
    scopes : List[Any]
        Array of scopes accessible to current user.
    roles : List[Any]
        Array of roles assigned to current user.
    """
    scopes: List[Any] = Field(..., alias='scopes')
    roles: List[Any] = Field(..., alias='roles')
