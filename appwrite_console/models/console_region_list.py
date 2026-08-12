from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .console_region import ConsoleRegion

class ConsoleRegionList(AppwriteModel):
    """
    Regions list

    Attributes
    ----------
    total : float
        Total number of regions that matched your query.
    regions : List[ConsoleRegion]
        List of regions.
    """
    total: float = Field(..., alias='total')
    regions: List[ConsoleRegion] = Field(..., alias='regions')
