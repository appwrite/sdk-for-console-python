from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .metric import Metric
from .usage_organization_project import UsageOrganizationProject

class UsageOrganization(AppwriteModel):
    """
    Organization

    Attributes
    ----------
    bandwidth : List[Metric]
        Aggregated stats for number of requests.
    users : List[Metric]
        Aggregated stats for consumed bandwidth.
    executions : List[Metric]
        Aggregated stats for function executions.
    databasesreads : List[Metric]
        Aggregated stats for database reads.
    databaseswrites : List[Metric]
        Aggregated stats for database writes.
    imagetransformations : List[Metric]
        Aggregated stats for file transformations.
    imagetransformationstotal : float
        Aggregated stats for total file transformations.
    screenshotsgenerated : List[Metric]
        Aggregated stats for file transformations.
    screenshotsgeneratedtotal : float
        Aggregated stats for total file transformations.
    userstotal : float
        Aggregated stats for total users.
    executionstotal : float
        Aggregated stats for total executions.
    executionsmbsecondstotal : float
        Aggregated stats for function executions in mb seconds.
    buildsmbsecondstotal : float
        Aggregated stats for function builds in mb seconds.
    filesstoragetotal : float
        Aggregated stats for total file storage.
    buildsstoragetotal : float
        Aggregated stats for total builds storage.
    deploymentsstoragetotal : float
        Aggregated stats for total deployments storage.
    databasesstoragetotal : float
        Aggregated stats for total databases storage.
    databasesreadstotal : float
        Aggregated stats for total databases  reads.
    databaseswritestotal : float
        Aggregated stats for total databases  writes.
    backupsstoragetotal : float
        Aggregated stats for total backups storage.
    storagetotal : float
        Aggregated stats for total storage.
    authphonetotal : float
        Aggregated stats for total auth phone.
    authphoneestimate : float
        Aggregated stats for total auth phone estimation.
    projects : List[UsageOrganizationProject]
        Aggregated stats for each projects.
    realtimeconnections : List[Metric]
        Aggregated stats for realtime connections.
    realtimeconnectionstotal : float
        Aggregated stats for total realtime connections.
    realtimemessages : List[Metric]
        Aggregated stats for realtime messages.
    realtimemessagestotal : float
        Aggregated stats for total realtime messages.
    realtimebandwidth : List[Metric]
        Aggregated stats for realtime bandwidth.
    realtimebandwidthtotal : float
        Aggregated stats for total realtime bandwidth.
    """
    bandwidth: List[Metric] = Field(..., alias='bandwidth')
    users: List[Metric] = Field(..., alias='users')
    executions: List[Metric] = Field(..., alias='executions')
    databasesreads: List[Metric] = Field(..., alias='databasesReads')
    databaseswrites: List[Metric] = Field(..., alias='databasesWrites')
    imagetransformations: List[Metric] = Field(..., alias='imageTransformations')
    imagetransformationstotal: float = Field(..., alias='imageTransformationsTotal')
    screenshotsgenerated: List[Metric] = Field(..., alias='screenshotsGenerated')
    screenshotsgeneratedtotal: float = Field(..., alias='screenshotsGeneratedTotal')
    userstotal: float = Field(..., alias='usersTotal')
    executionstotal: float = Field(..., alias='executionsTotal')
    executionsmbsecondstotal: float = Field(..., alias='executionsMBSecondsTotal')
    buildsmbsecondstotal: float = Field(..., alias='buildsMBSecondsTotal')
    filesstoragetotal: float = Field(..., alias='filesStorageTotal')
    buildsstoragetotal: float = Field(..., alias='buildsStorageTotal')
    deploymentsstoragetotal: float = Field(..., alias='deploymentsStorageTotal')
    databasesstoragetotal: float = Field(..., alias='databasesStorageTotal')
    databasesreadstotal: float = Field(..., alias='databasesReadsTotal')
    databaseswritestotal: float = Field(..., alias='databasesWritesTotal')
    backupsstoragetotal: float = Field(..., alias='backupsStorageTotal')
    storagetotal: float = Field(..., alias='storageTotal')
    authphonetotal: float = Field(..., alias='authPhoneTotal')
    authphoneestimate: float = Field(..., alias='authPhoneEstimate')
    projects: List[UsageOrganizationProject] = Field(..., alias='projects')
    realtimeconnections: List[Metric] = Field(..., alias='realtimeConnections')
    realtimeconnectionstotal: float = Field(..., alias='realtimeConnectionsTotal')
    realtimemessages: List[Metric] = Field(..., alias='realtimeMessages')
    realtimemessagestotal: float = Field(..., alias='realtimeMessagesTotal')
    realtimebandwidth: List[Metric] = Field(..., alias='realtimeBandwidth')
    realtimebandwidthtotal: float = Field(..., alias='realtimeBandwidthTotal')
