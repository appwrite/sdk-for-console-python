from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_member import DedicatedDatabaseMember

class DedicatedDatabaseReplicas(AppwriteModel):
    """
    Replicas

    Attributes
    ----------
    replicas : float
        Number of configured replicas. Zero means high availability is disabled.
    syncmode : str
        Requested replication sync mode. Possible values: async (asynchronous, fastest), sync (synchronous, strong consistency), quorum (quorum-based, majority of replicas must confirm). This is what was asked for; compare it with effectiveSyncMode for what the primary is enforcing.
    effectivesyncmode : Optional[str]
        Replication sync mode the primary is actually enforcing. Null when high availability is disabled or the state could not be read. A value below the requested syncMode means writes are being acknowledged with weaker durability than configured.
    syncdegraded : bool
        Whether the enforced replication is weaker than the requested syncMode.
    syncacknowledgements : float
        Number of standby acknowledgements the primary waits for before a write is committed. Zero means writes are acknowledged locally.
    syncstandbycount : float
        Number of standbys registered with the primary for synchronous replication.
    syncstateconfirmed : Optional[bool]
        Whether the reported sync state was read from the engine and corroborated. When false the engine was asked and the state was not corroborated, which happens two ways: the configuration probe did not answer, in which case the other sync fields carry no reading; or it answered and an active standby contradicted it or its replication stream could not be read, in which case the other sync fields do carry genuine engine readings. Absent when no engine was asked at all, so an unprobed database is distinguishable from an unconfirmed one — draw no conclusion about replication from a response that omits it.
    members : List[DedicatedDatabaseMember]
        Per-pod statuses for the primary and every replica.
    """
    replicas: float = Field(..., alias='replicas')
    syncmode: str = Field(..., alias='syncMode')
    effectivesyncmode: Optional[str] = Field(default=None, alias='effectiveSyncMode')
    syncdegraded: bool = Field(..., alias='syncDegraded')
    syncacknowledgements: float = Field(..., alias='syncAcknowledgements')
    syncstandbycount: float = Field(..., alias='syncStandbyCount')
    syncstateconfirmed: Optional[bool] = Field(default=None, alias='syncStateConfirmed')
    members: List[DedicatedDatabaseMember] = Field(..., alias='members')
