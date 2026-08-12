from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .dev_key import DevKey

class DevKeyList(AppwriteModel):
    """
    Dev Keys List

    Attributes
    ----------
    total : float
        Total number of devKeys that matched your query.
    devkeys : List[DevKey]
        List of devKeys.
    """
    total: float = Field(..., alias='total')
    devkeys: List[DevKey] = Field(..., alias='devKeys')
