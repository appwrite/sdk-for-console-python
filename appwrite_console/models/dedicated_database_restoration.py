from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DedicatedDatabaseRestoration(AppwriteModel):
    """
    Restoration

    Attributes
    ----------
    id : str
        Restoration ID.
    createdat : str
        Restoration creation time in ISO 8601 format.
    databaseid : str
        Database ID being restored into.
    sourcedatabaseid : Optional[str]
        Source database ID when restoring a backup into another database.
    projectid : str
        Project ID.
    backupid : Optional[str]
        Backup ID used for restoration (null for PITR).
    type : str
        Restoration type. Possible values: backup (restore from a specific backup snapshot), pitr (point-in-time recovery to a specific timestamp).
    status : str
        Restoration status. Possible values: pending (queued for processing), running (currently in progress), completed (successfully finished), failed (encountered an error).
    targettime : Optional[str]
        Target time for PITR restoration in ISO 8601 format.
    startedat : Optional[str]
        Restoration start time in ISO 8601 format.
    completedat : Optional[str]
        Restoration completion time in ISO 8601 format.
    error : str
        Error message if restoration failed.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    databaseid: str = Field(..., alias='databaseId')
    sourcedatabaseid: Optional[str] = Field(default=None, alias='sourceDatabaseId')
    projectid: str = Field(..., alias='projectId')
    backupid: Optional[str] = Field(default=None, alias='backupId')
    type: str = Field(..., alias='type')
    status: str = Field(..., alias='status')
    targettime: Optional[str] = Field(default=None, alias='targetTime')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    completedat: Optional[str] = Field(default=None, alias='completedAt')
    error: str = Field(..., alias='error')
