from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class Branch(AppwriteModel):
    """
    Branch

    Attributes
    ----------
    name : str
        Branch Name.
    """

    name: str = Field(
        ...,
        alias='name',
    )
