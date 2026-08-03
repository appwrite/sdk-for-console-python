from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DatabaseMigration(AppwriteModel):
    """
    Database Migration

    Attributes
    ----------
    id : str
        Database migration ID.
    createdat : str
        Migration creation time in ISO 8601 format.
    updatedat : str
        Migration update time in ISO 8601 format.
    projectid : str
        Project ID that owns the migrating database.
    databaseid : str
        Logical database ID being migrated.
    specification : str
        Dedicated compute specification provisioned for the migration target.
    phase : str
        Migration phase. Possible values: pending, provisioned, capturing, backfilling, catching_up, verifying, ready_to_cutover, cutover, soaking, done, failed, rolled_back.
    attempt : float
        Number of times a migration step has failed and been recorded.
    lasterror : str
        Reason the most recent migration step failed, empty while none has.
    lagdocuments : float
        Number of documents still pending replication to the target.
    verifiedat : str
        Time the migrated data was verified against the source in ISO 8601 format.
    cutoverat : str
        Time routing was flipped to the target in ISO 8601 format.
    soakuntil : str
        Time the post-cutover soak window ends in ISO 8601 format.
    autocutover : bool
        Whether the migration cuts over automatically once ready.
    paused : bool
        Whether the migration is paused.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    projectid: str = Field(..., alias='projectId')
    databaseid: str = Field(..., alias='databaseId')
    specification: str = Field(..., alias='specification')
    phase: str = Field(..., alias='phase')
    attempt: float = Field(..., alias='attempt')
    lasterror: str = Field(..., alias='lastError')
    lagdocuments: float = Field(..., alias='lagDocuments')
    verifiedat: str = Field(..., alias='verifiedAt')
    cutoverat: str = Field(..., alias='cutoverAt')
    soakuntil: str = Field(..., alias='soakUntil')
    autocutover: bool = Field(..., alias='autoCutover')
    paused: bool = Field(..., alias='paused')
