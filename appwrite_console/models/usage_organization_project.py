from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class UsageOrganizationProject(AppwriteModel):
    """
    OrganizationProject

    Attributes
    ----------
    projectid : str
        projectId
    bandwidth : float
        Aggregated stats for number of requests.
    users : float
        Aggregated stats for consumed bandwidth.
    executions : float
        Aggregated stats for function executions.
    databasesreads : float
        Aggregated stats for database reads.
    databaseswrites : float
        Aggregated stats for database writes.
    executionsmbseconds : float
        Aggregated stats for function executions in mb seconds.
    buildsmbseconds : float
        Aggregated stats for function builds in mb seconds.
    storage : float
        Aggregated stats for number of documents.
    authphonetotal : float
        Aggregated stats for phone authentication.
    authphoneestimate : float
        Aggregated stats for phone authentication estimated cost.
    databasesreadstotal : float
        Aggregated stats for total databases reads.
    databaseswritestotal : float
        Aggregated stats for total databases writes.
    imagetransformations : float
        Aggregated stats for file transformations.
    imagetransformationstotal : float
        Aggregated stats for total file transformations.
    screenshotsgenerated : float
        Aggregated stats for file transformations.
    screenshotsgeneratedtotal : float
        Aggregated stats for total file transformations.
    realtimeconnections : float
        Aggregated stats for realtime connections.
    realtimemessages : float
        Aggregated stats for realtime messages.
    realtimebandwidth : float
        Aggregated stats for realtime bandwidth.
    """

    projectid: str = Field(
        ...,
        alias='projectId',
    )
    bandwidth: float = Field(
        ...,
        alias='bandwidth',
    )
    users: float = Field(
        ...,
        alias='users',
    )
    executions: float = Field(
        ...,
        alias='executions',
    )
    databasesreads: float = Field(
        ...,
        alias='databasesReads',
    )
    databaseswrites: float = Field(
        ...,
        alias='databasesWrites',
    )
    executionsmbseconds: float = Field(
        ...,
        alias='executionsMBSeconds',
    )
    buildsmbseconds: float = Field(
        ...,
        alias='buildsMBSeconds',
    )
    storage: float = Field(
        ...,
        alias='storage',
    )
    authphonetotal: float = Field(
        ...,
        alias='authPhoneTotal',
    )
    authphoneestimate: float = Field(
        ...,
        alias='authPhoneEstimate',
    )
    databasesreadstotal: float = Field(
        ...,
        alias='databasesReadsTotal',
    )
    databaseswritestotal: float = Field(
        ...,
        alias='databasesWritesTotal',
    )
    imagetransformations: float = Field(
        ...,
        alias='imageTransformations',
    )
    imagetransformationstotal: float = Field(
        ...,
        alias='imageTransformationsTotal',
    )
    screenshotsgenerated: float = Field(
        ...,
        alias='screenshotsGenerated',
    )
    screenshotsgeneratedtotal: float = Field(
        ...,
        alias='screenshotsGeneratedTotal',
    )
    realtimeconnections: float = Field(
        ...,
        alias='realtimeConnections',
    )
    realtimemessages: float = Field(
        ...,
        alias='realtimeMessages',
    )
    realtimebandwidth: float = Field(
        ...,
        alias='realtimeBandwidth',
    )
