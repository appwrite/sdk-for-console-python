from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Migration(AppwriteModel):
    """
    Migration

    Attributes
    ----------
    id : str
        Migration ID.
    createdat : str
        Migration creation date in ISO 8601 format.
    updatedat : str
        Variable creation date in ISO 8601 format.
    status : str
        Migration status ( pending, processing, failed, completed ) 
    stage : str
        Migration stage ( init, processing, source-check, destination-check, migrating, finished )
    source : str
        A string containing the type of source of the migration.
    destination : str
        A string containing the type of destination of the migration.
    resources : List[Any]
        Resources to migrate.
    resourceid : str
        ID of the resource being migrated.
    resourceinternalid : str
        Internal ID of the resource being migrated.
    resourcetype : str
        Type of the resource being migrated.
    parentresourceid : str
        ID of the parent resource that contains the migrated resource.
    parentresourceinternalid : str
        Internal ID of the parent resource that contains the migrated resource.
    parentresourcetype : str
        Type of the parent resource that contains the migrated resource.
    destinationresourceid : str
        ID of the destination resource created or overwritten by the migration.
    destinationresourceinternalid : str
        Internal ID of the destination resource created or overwritten by the migration.
    destinationresourcetype : str
        Type of the destination resource created or overwritten by the migration.
    statuscounters : Dict[str, Any]
        A group of counters that represent the total progress of the migration.
    resourcedata : Dict[str, Any]
        An array of objects containing the report data of the resources that were migrated.
    errors : List[Any]
        All errors that occurred during the migration process.
    options : Dict[str, Any]
        Migration options used during the migration process.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    status: str = Field(..., alias='status')
    stage: str = Field(..., alias='stage')
    source: str = Field(..., alias='source')
    destination: str = Field(..., alias='destination')
    resources: List[Any] = Field(..., alias='resources')
    resourceid: str = Field(..., alias='resourceId')
    resourceinternalid: str = Field(..., alias='resourceInternalId')
    resourcetype: str = Field(..., alias='resourceType')
    parentresourceid: str = Field(..., alias='parentResourceId')
    parentresourceinternalid: str = Field(..., alias='parentResourceInternalId')
    parentresourcetype: str = Field(..., alias='parentResourceType')
    destinationresourceid: str = Field(..., alias='destinationResourceId')
    destinationresourceinternalid: str = Field(..., alias='destinationResourceInternalId')
    destinationresourcetype: str = Field(..., alias='destinationResourceType')
    statuscounters: Dict[str, Any] = Field(..., alias='statusCounters')
    resourcedata: Dict[str, Any] = Field(..., alias='resourceData')
    errors: List[Any] = Field(..., alias='errors')
    options: Dict[str, Any] = Field(..., alias='options')
