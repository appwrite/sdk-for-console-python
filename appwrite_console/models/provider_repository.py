from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class ProviderRepository(AppwriteModel):
    """
    ProviderRepository

    Attributes
    ----------
    id : str
        VCS (Version Control System) repository ID.
    name : str
        VCS (Version Control System) repository name.
    organization : str
        VCS (Version Control System) organization name
    provider : str
        VCS (Version Control System) provider name.
    private : bool
        Is VCS (Version Control System) repository private?
    defaultbranch : str
        VCS (Version Control System) repository&#039;s default branch name.
    providerinstallationid : str
        VCS (Version Control System) installation ID.
    authorized : bool
        Is VCS (Version Control System) repository authorized for the installation?
    pushedat : str
        Last commit date in ISO 8601 format.
    variables : List[Any]
        Environment variables found in .env files
    """
    id: str = Field(..., alias='id')
    name: str = Field(..., alias='name')
    organization: str = Field(..., alias='organization')
    provider: str = Field(..., alias='provider')
    private: bool = Field(..., alias='private')
    defaultbranch: str = Field(..., alias='defaultBranch')
    providerinstallationid: str = Field(..., alias='providerInstallationId')
    authorized: bool = Field(..., alias='authorized')
    pushedat: str = Field(..., alias='pushedAt')
    variables: List[Any] = Field(..., alias='variables')
