from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class DomainPrice(AppwriteModel):
    """
    DomainPrice

    Attributes
    ----------
    domain : str
        Domain name.
    tld : str
        Top-level domain for the requested domain.
    available : bool
        Whether the domain is currently available for registration.
    price : float
        Domain registration price.
    periodyears : float
        Price period in years.
    premium : bool
        Whether the domain is a premium domain.
    """
    domain: str = Field(..., alias='domain')
    tld: str = Field(..., alias='tld')
    available: bool = Field(..., alias='available')
    price: float = Field(..., alias='price')
    periodyears: float = Field(..., alias='periodYears')
    premium: bool = Field(..., alias='premium')
