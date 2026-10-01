from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_specification import DedicatedDatabaseSpecification


class DedicatedDatabaseSpecificationList(AppwriteModel):
    """
    SpecificationList

    Attributes
    ----------
    specifications : List[DedicatedDatabaseSpecification]
        List of dedicated database specifications.
    total : float
        Total number of specifications.
    """

    specifications: List[DedicatedDatabaseSpecification] = Field(..., alias='specifications')
    total: float = Field(..., alias='total')
