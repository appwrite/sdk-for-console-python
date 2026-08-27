from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DetectionVariable(AppwriteModel):
    """
    DetectionVariable

    Attributes
    ----------
    name : str
        Name of environment variable
    value : str
        Value of environment variable
    """

    name: str = Field(
        ...,
        alias='name',
    )
    value: str = Field(
        ...,
        alias='value',
    )
