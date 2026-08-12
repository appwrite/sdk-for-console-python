from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Installation(AppwriteModel):
    """
    Installation

    Attributes
    ----------
    id : str
        Function ID.
    createdat : str
        Function creation date in ISO 8601 format.
    updatedat : str
        Function update date in ISO 8601 format.
    provider : str
        VCS (Version Control System) provider name.
    organization : str
        VCS (Version Control System) organization name.
    providerinstallationid : str
        VCS (Version Control System) installation ID.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    provider: str = Field(..., alias='provider')
    organization: str = Field(..., alias='organization')
    providerinstallationid: str = Field(..., alias='providerInstallationId')
