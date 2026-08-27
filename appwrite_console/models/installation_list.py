from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .installation import Installation


class InstallationList(AppwriteModel):
    """
    Installations List

    Attributes
    ----------
    total : float
        Total number of installations that matched your query.
    installations : List[Installation]
        List of installations.
    """

    total: float = Field(..., alias='total')
    installations: List[Installation] = Field(..., alias='installations')
