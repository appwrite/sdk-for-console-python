from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class ConsoleKeyScope(AppwriteModel):
    """
    Console Key Scope

    Attributes
    ----------
    id : str
        Scope ID.
    description : str
        Scope description.
    category : str
        Scope category.
    deprecated : bool
        Scope is deprecated.
    """
    id: str = Field(..., alias='$id')
    description: str = Field(..., alias='description')
    category: str = Field(..., alias='category')
    deprecated: bool = Field(..., alias='deprecated')
