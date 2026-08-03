from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class TemplateFramework(AppwriteModel):
    """
    Template Framework

    Attributes
    ----------
    key : str
        Parent framework key.
    name : str
        Framework Name.
    installcommand : str
        The install command used to install the dependencies.
    buildcommand : str
        The build command used to build the deployment.
    outputdirectory : str
        The output directory to store the build output.
    providerrootdirectory : str
        Path to site in VCS (Version Control System) repository
    buildruntime : str
        Runtime used during build step of template.
    adapter : str
        Site framework runtime
    fallbackfile : str
        Fallback file for SPA. Only relevant for static serve runtime.
    """
    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    installcommand: str = Field(..., alias='installCommand')
    buildcommand: str = Field(..., alias='buildCommand')
    outputdirectory: str = Field(..., alias='outputDirectory')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
    buildruntime: str = Field(..., alias='buildRuntime')
    adapter: str = Field(..., alias='adapter')
    fallbackfile: str = Field(..., alias='fallbackFile')
