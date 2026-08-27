from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.detection_framework_type import DetectionFrameworkType
from .detection_variable import DetectionVariable


class DetectionFramework(AppwriteModel):
    """
    DetectionFramework

    Attributes
    ----------
    type : DetectionFrameworkType
        Repository detection type.
    variables : Optional[List[DetectionVariable]]
        Environment variables found in .env files
    framework : str
        Framework
    installcommand : str
        Site Install Command
    buildcommand : str
        Site Build Command
    outputdirectory : str
        Site Output Directory
    """

    type: DetectionFrameworkType = Field(..., alias='type')
    variables: Optional[List[DetectionVariable]] = Field(default=None, alias='variables')
    framework: str = Field(..., alias='framework')
    installcommand: str = Field(..., alias='installCommand')
    buildcommand: str = Field(..., alias='buildCommand')
    outputdirectory: str = Field(..., alias='outputDirectory')
