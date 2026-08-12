from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .metric import Metric

class UsageOrganizationProject(AppwriteModel):
    """
    OrganizationProject

    Attributes
    ----------
    projectid : str
        projectId
    bandwidth : List[Metric]
        Aggregated stats for number of requests.
    users : List[Metric]
        Aggregated stats for consumed bandwidth.
    executions : float
        Aggregated stats for function executions.
    databasesreads : List[Metric]
        Aggregated stats for database reads.
    databaseswrites : List[Metric]
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
    imagetransformations : List[Metric]
        Aggregated stats for file transformations.
    imagetransformationstotal : float
        Aggregated stats for total file transformations.
    screenshotsgenerated : List[Metric]
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
    projectid: str = Field(..., alias='projectId')
    bandwidth: List[Metric] = Field(..., alias='bandwidth')
    users: List[Metric] = Field(..., alias='users')
    executions: float = Field(..., alias='executions')
    databasesreads: List[Metric] = Field(..., alias='databasesReads')
    databaseswrites: List[Metric] = Field(..., alias='databasesWrites')
    executionsmbseconds: float = Field(..., alias='executionsMBSeconds')
    buildsmbseconds: float = Field(..., alias='buildsMBSeconds')
    storage: float = Field(..., alias='storage')
    authphonetotal: float = Field(..., alias='authPhoneTotal')
    authphoneestimate: float = Field(..., alias='authPhoneEstimate')
    databasesreadstotal: float = Field(..., alias='databasesReadsTotal')
    databaseswritestotal: float = Field(..., alias='databasesWritesTotal')
    imagetransformations: List[Metric] = Field(..., alias='imageTransformations')
    imagetransformationstotal: float = Field(..., alias='imageTransformationsTotal')
    screenshotsgenerated: List[Metric] = Field(..., alias='screenshotsGenerated')
    screenshotsgeneratedtotal: float = Field(..., alias='screenshotsGeneratedTotal')
    realtimeconnections: float = Field(..., alias='realtimeConnections')
    realtimemessages: float = Field(..., alias='realtimeMessages')
    realtimebandwidth: float = Field(..., alias='realtimeBandwidth')
