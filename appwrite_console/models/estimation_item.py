from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class EstimationItem(AppwriteModel):
    """
    Item

    Attributes
    ----------
    label : str
        Label
    value : float
        Gross payable amount
    """
    label: str = Field(..., alias='label')
    value: float = Field(..., alias='value')
