from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class UsageResources(AppwriteModel):
    """
    Resource

    Attributes
    ----------
    name : str
        Invoice name
    value : float
        Invoice value
    amount : float
        Invoice amount
    rate : float
        Invoice rate
    desc : str
        Invoice description
    resourceid : str
        Resource ID
    type : str
        Dedicated database engine type for per-database line items (e.g. postgresql). Empty for other resources.
    specification : str
        Dedicated database specification slug for per-database line items (e.g. s-2vcpu-2gb). Empty for other resources.
    """
    name: str = Field(..., alias='name')
    value: float = Field(..., alias='value')
    amount: float = Field(..., alias='amount')
    rate: float = Field(..., alias='rate')
    desc: str = Field(..., alias='desc')
    resourceid: str = Field(..., alias='resourceId')
    type: str = Field(..., alias='type')
    specification: str = Field(..., alias='specification')
