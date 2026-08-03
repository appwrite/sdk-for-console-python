from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .database_status_connections import DatabaseStatusConnections
from .database_status_replica import DatabaseStatusReplica
from .database_status_volume import DatabaseStatusVolume

class DatabaseStatus(AppwriteModel):
    """
    Status

    Attributes
    ----------
    health : str
        Overall health status: healthy, degraded, or unhealthy.
    ready : bool
        Whether the database is ready to accept connections.
    engine : str
        Database engine: postgresql, mysql, or mongodb.
    version : str
        Database engine version.
    uptime : float
        Database uptime in seconds.
    connections : DatabaseStatusConnections
        Connection statistics.
    syncmode : str
        Requested replication sync mode. Possible values: async, sync, quorum. Compare with effectiveSyncMode for what the primary is enforcing.
    effectivesyncmode : Optional[str]
        Replication sync mode the primary is actually enforcing. Null when high availability is disabled or the state could not be read.
    syncdegraded : bool
        Whether the enforced replication is weaker than the requested syncMode.
    syncacknowledgements : float
        Number of standby acknowledgements the primary waits for before a write is committed.
    syncstandbycount : float
        Number of standbys registered with the primary for synchronous replication.
    syncstateconfirmed : bool
        Whether the reported sync state was read from the engine. When false the state could not be confirmed and the other sync fields carry no reading.
    replicas : List[DatabaseStatusReplica]
        List of database replicas and their status. Every configured member appears, including one the backend has not brought up, which is reported as not healthy.
    volumes : List[DatabaseStatusVolume]
        Storage volume information.
    """
    health: str = Field(..., alias='health')
    ready: bool = Field(..., alias='ready')
    engine: str = Field(..., alias='engine')
    version: str = Field(..., alias='version')
    uptime: float = Field(..., alias='uptime')
    connections: DatabaseStatusConnections = Field(..., alias='connections')
    syncmode: str = Field(..., alias='syncMode')
    effectivesyncmode: Optional[str] = Field(default=None, alias='effectiveSyncMode')
    syncdegraded: bool = Field(..., alias='syncDegraded')
    syncacknowledgements: float = Field(..., alias='syncAcknowledgements')
    syncstandbycount: float = Field(..., alias='syncStandbyCount')
    syncstateconfirmed: bool = Field(..., alias='syncStateConfirmed')
    replicas: List[DatabaseStatusReplica] = Field(..., alias='replicas')
    volumes: List[DatabaseStatusVolume] = Field(..., alias='volumes')
