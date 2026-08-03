from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .block import Block

class BlockDelete(AppwriteModel):
    """
    BlockDelete

    Attributes
    ----------
    deleted : float
        Number of blocks deleted
    blocks : List[Block]
        List of deleted blocks
    """
    deleted: float = Field(..., alias='deleted')
    blocks: List[Block] = Field(..., alias='blocks')
