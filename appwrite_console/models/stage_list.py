from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .stage import Stage


class StageList(AppwriteModel):
    """
    Stages List

    Attributes
    ----------
    stages : List[Stage]
        List of stages.
    """

    stages: List[Stage] = Field(..., alias='stages')
