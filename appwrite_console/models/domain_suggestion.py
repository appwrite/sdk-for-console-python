from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class DomainSuggestion(AppwriteModel):
    """
    DomainSuggestion

    Attributes
    ----------
    domain : str
        Domain suggestion.
    premium : bool
        Is the domain premium?
    price : Optional[float]
        Domain price.
    available : bool
        Is the domain available?
    """
    domain: str = Field(..., alias='domain')
    premium: bool = Field(..., alias='premium')
    price: Optional[float] = Field(default=None, alias='price')
    available: bool = Field(..., alias='available')
