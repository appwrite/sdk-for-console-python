from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .block import Block

class BlockList(AppwriteModel):
    """
    Blocks list

    Attributes
    ----------
    total : float
        Total number of blocks that matched your query.
    blocks : List[Block]
        List of blocks.
    """
    total: float = Field(..., alias='total')
    blocks: List[Block] = Field(..., alias='blocks')
