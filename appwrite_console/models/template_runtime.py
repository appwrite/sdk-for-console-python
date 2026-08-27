from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class TemplateRuntime(AppwriteModel):
    """
    Template Runtime

    Attributes
    ----------
    name : str
        Runtime Name.
    commands : str
        The build command used to build the deployment.
    entrypoint : str
        The entrypoint file used to execute the deployment.
    providerrootdirectory : str
        Path to function in VCS (Version Control System) repository
    """

    name: str = Field(..., alias='name')
    commands: str = Field(..., alias='commands')
    entrypoint: str = Field(..., alias='entrypoint')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
