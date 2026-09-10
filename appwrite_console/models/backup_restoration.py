from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class BackupRestoration(AppwriteModel):
    """
    Restoration

    Attributes
    ----------
    id : str
        Restoration ID.
    createdat : str
        Restoration creation time in ISO 8601 format.
    updatedat : str
        Restoration update date in ISO 8601 format.
    archiveid : str
        Backup archive ID.
    policyid : Optional[str]
        Backup policy ID.
    status : str
        The status of the restoration. Possible values: pending, downloading, processing, completed, failed.
    startedat : Optional[str]
        The backup start time.
    migrationid : str
        Migration ID.
    services : List[Any]
        The services that are backed up by this policy.
    resources : List[Any]
        The resources that are backed up by this policy.
    options : Dict[str, Any]
        Resource mappings used by the restoration.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    archiveid: str = Field(..., alias='archiveId')
    policyid: Optional[str] = Field(default=None, alias='policyId')
    status: str = Field(..., alias='status')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    migrationid: str = Field(..., alias='migrationId')
    services: List[Any] = Field(..., alias='services')
    resources: List[Any] = Field(..., alias='resources')
    options: Dict[str, Any] = Field(..., alias='options')
