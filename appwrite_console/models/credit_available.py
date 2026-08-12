from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class CreditAvailable(AppwriteModel):
    """
    CreditAvailable

    Attributes
    ----------
    available : float
        Total available credits for the organization.
    """
    available: float = Field(..., alias='available')
