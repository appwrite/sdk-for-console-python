from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .branch import Branch

class BranchList(AppwriteModel):
    """
    Branches List

    Attributes
    ----------
    total : float
        Total number of branches that matched your query.
    branches : List[Branch]
        List of branches.
    """
    total: float = Field(..., alias='total')
    branches: List[Branch] = Field(..., alias='branches')
