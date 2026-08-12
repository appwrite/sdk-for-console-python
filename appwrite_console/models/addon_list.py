from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .addon import Addon

class AddonList(AppwriteModel):
    """
    Addons list

    Attributes
    ----------
    total : float
        Total number of addons that matched your query.
    addons : List[Addon]
        List of addons.
    """
    total: float = Field(..., alias='total')
    addons: List[Addon] = Field(..., alias='addons')
