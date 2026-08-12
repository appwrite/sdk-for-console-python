from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .metric import Metric
from .metric_breakdown import MetricBreakdown

class UsageProject(AppwriteModel):
    """
    Project

    Attributes
    ----------
    executionstotal : float
        Total aggregated number of function executions.
    documentstotal : float
        Total aggregated  number of documents in legacy/tablesdb.
    documentsdbdocumentstotal : float
        Total aggregated  number of documents in documentsdb.
    rowstotal : float
        Total aggregated  number of rows.
    databasestotal : float
        Total aggregated number of databases.
    documentsdbtotal : float
        Total aggregated number of documentsdb.
    databasesstoragetotal : float
        Total aggregated sum of databases storage size (in bytes).
    documentsdbdatabasesstoragetotal : float
        Total aggregated sum of documentsdb databases storage size (in bytes).
    userstotal : float
        Total aggregated number of users.
    filesstoragetotal : float
        Total aggregated sum of files storage size (in bytes).
    functionsstoragetotal : float
        Total aggregated sum of functions storage size (in bytes).
    buildsstoragetotal : float
        Total aggregated sum of builds storage size (in bytes).
    deploymentsstoragetotal : float
        Total aggregated sum of deployments storage size (in bytes).
    bucketstotal : float
        Total aggregated number of buckets.
    executionsmbsecondstotal : float
        Total aggregated number of function executions mbSeconds.
    buildsmbsecondstotal : float
        Total aggregated number of function builds mbSeconds.
    databasesreadstotal : float
        Aggregated stats for total databases reads.
    databaseswritestotal : float
        Aggregated stats for total databases writes.
    documentsdbdatabasesreadstotal : float
        Total number of documentsdb databases reads.
    documentsdbdatabaseswritestotal : float
        Total number of documentsdb databases writes.
    requests : List[Metric]
        Aggregated  number of requests per period.
    network : List[Metric]
        Aggregated number of consumed bandwidth per period.
    users : List[Metric]
        Aggregated number of users per period.
    executions : List[Metric]
        Aggregated number of executions per period.
    authphonetotal : float
        Aggregated stats for total auth phone.
    authphoneestimate : float
        Aggregated stats for total auth phone estimation.
    authphonecountrybreakdown : List[MetricBreakdown]
        Aggregated breakdown in totals of phone auth by country.
    databasesreads : List[Metric]
        Aggregated stats for database reads.
    databaseswrites : List[Metric]
        Aggregated stats for database writes.
    documentsdbdatabasesreads : List[Metric]
        An array of aggregated number of documentsdb database reads.
    documentsdbdatabaseswrites : List[Metric]
        An array of aggregated number of documentsdb database writes.
    documentsdbdatabasesstorage : List[Metric]
        An array of aggregated sum of documentsdb databases storage size (in bytes) per period.
    imagetransformations : List[Metric]
        An array of aggregated number of image transformations.
    imagetransformationstotal : float
        Total aggregated number of image transformations.
    vectorsdbdatabasestotal : float
        Total aggregated number of VectorsDB databases.
    vectorsdbcollectionstotal : float
        Total aggregated number of VectorsDB collections.
    vectorsdbdocumentstotal : float
        Total aggregated number of VectorsDB documents.
    vectorsdbdatabasesstoragetotal : float
        Total aggregated VectorsDB storage (bytes).
    vectorsdbdatabasesreadstotal : float
        Total aggregated number of VectorsDB reads.
    vectorsdbdatabaseswritestotal : float
        Total aggregated number of VectorsDB writes.
    vectorsdbdatabases : List[Metric]
        Aggregated VectorsDB databases per period.
    vectorsdbcollections : List[Metric]
        Aggregated VectorsDB collections per period.
    vectorsdbdocuments : List[Metric]
        Aggregated VectorsDB documents per period.
    vectorsdbdatabasesstorage : List[Metric]
        Aggregated VectorsDB storage per period.
    vectorsdbdatabasesreads : List[Metric]
        Aggregated VectorsDB reads per period.
    vectorsdbdatabaseswrites : List[Metric]
        Aggregated VectorsDB writes per period.
    embeddingstext : List[Metric]
        Aggregated number of text embedding calls per period.
    embeddingstexttokens : List[Metric]
        Aggregated number of tokens processed by text embeddings per period.
    embeddingstextduration : List[Metric]
        Aggregated duration spent generating text embeddings per period.
    embeddingstexterrors : List[Metric]
        Aggregated number of errors while generating text embeddings per period.
    embeddingstexttotal : float
        Total aggregated number of text embedding calls.
    embeddingstexttokenstotal : float
        Total aggregated number of tokens processed by text.
    embeddingstextdurationtotal : float
        Total aggregated duration spent generating text embeddings.
    embeddingstexterrorstotal : float
        Total aggregated number of errors while generating text embeddings.
    functionsexecutions : List[Metric]
        Aggregated number of function executions per period.
    functionsexecutionstotal : float
        Total aggregated number of function executions.
    sitesexecutions : List[Metric]
        Aggregated number of site executions per period.
    sitesexecutionstotal : float
        Total aggregated number of site executions.
    networktotal : float
        Aggregated stats for total network bandwidth.
    backupsstoragetotal : float
        Aggregated stats for total backups storage.
    screenshotsgenerated : List[Metric]
        An array of aggregated number of screenshots generated.
    screenshotsgeneratedtotal : float
        Total aggregated number of screenshots generated.
    realtimeconnectionstotal : float
        Current aggregated number of open Realtime connections.
    realtimemessagestotal : float
        Total number of Realtime messages sent to clients.
    realtimebandwidthtotal : float
        Total consumed Realtime bandwidth (in bytes).
    realtimeconnections : List[Metric]
        Aggregated number of open Realtime connections per period.
    realtimemessages : List[Metric]
        Aggregated number of Realtime messages sent to clients per period.
    realtimebandwidth : List[Metric]
        Aggregated consumed Realtime bandwidth (in bytes) per period.
    """
    executionstotal: float = Field(..., alias='executionsTotal')
    documentstotal: float = Field(..., alias='documentsTotal')
    documentsdbdocumentstotal: float = Field(..., alias='documentsdbDocumentsTotal')
    rowstotal: float = Field(..., alias='rowsTotal')
    databasestotal: float = Field(..., alias='databasesTotal')
    documentsdbtotal: float = Field(..., alias='documentsdbTotal')
    databasesstoragetotal: float = Field(..., alias='databasesStorageTotal')
    documentsdbdatabasesstoragetotal: float = Field(..., alias='documentsdbDatabasesStorageTotal')
    userstotal: float = Field(..., alias='usersTotal')
    filesstoragetotal: float = Field(..., alias='filesStorageTotal')
    functionsstoragetotal: float = Field(..., alias='functionsStorageTotal')
    buildsstoragetotal: float = Field(..., alias='buildsStorageTotal')
    deploymentsstoragetotal: float = Field(..., alias='deploymentsStorageTotal')
    bucketstotal: float = Field(..., alias='bucketsTotal')
    executionsmbsecondstotal: float = Field(..., alias='executionsMbSecondsTotal')
    buildsmbsecondstotal: float = Field(..., alias='buildsMbSecondsTotal')
    databasesreadstotal: float = Field(..., alias='databasesReadsTotal')
    databaseswritestotal: float = Field(..., alias='databasesWritesTotal')
    documentsdbdatabasesreadstotal: float = Field(..., alias='documentsdbDatabasesReadsTotal')
    documentsdbdatabaseswritestotal: float = Field(..., alias='documentsdbDatabasesWritesTotal')
    requests: List[Metric] = Field(..., alias='requests')
    network: List[Metric] = Field(..., alias='network')
    users: List[Metric] = Field(..., alias='users')
    executions: List[Metric] = Field(..., alias='executions')
    authphonetotal: float = Field(..., alias='authPhoneTotal')
    authphoneestimate: float = Field(..., alias='authPhoneEstimate')
    authphonecountrybreakdown: List[MetricBreakdown] = Field(..., alias='authPhoneCountryBreakdown')
    databasesreads: List[Metric] = Field(..., alias='databasesReads')
    databaseswrites: List[Metric] = Field(..., alias='databasesWrites')
    documentsdbdatabasesreads: List[Metric] = Field(..., alias='documentsdbDatabasesReads')
    documentsdbdatabaseswrites: List[Metric] = Field(..., alias='documentsdbDatabasesWrites')
    documentsdbdatabasesstorage: List[Metric] = Field(..., alias='documentsdbDatabasesStorage')
    imagetransformations: List[Metric] = Field(..., alias='imageTransformations')
    imagetransformationstotal: float = Field(..., alias='imageTransformationsTotal')
    vectorsdbdatabasestotal: float = Field(..., alias='vectorsdbDatabasesTotal')
    vectorsdbcollectionstotal: float = Field(..., alias='vectorsdbCollectionsTotal')
    vectorsdbdocumentstotal: float = Field(..., alias='vectorsdbDocumentsTotal')
    vectorsdbdatabasesstoragetotal: float = Field(..., alias='vectorsdbDatabasesStorageTotal')
    vectorsdbdatabasesreadstotal: float = Field(..., alias='vectorsdbDatabasesReadsTotal')
    vectorsdbdatabaseswritestotal: float = Field(..., alias='vectorsdbDatabasesWritesTotal')
    vectorsdbdatabases: List[Metric] = Field(..., alias='vectorsdbDatabases')
    vectorsdbcollections: List[Metric] = Field(..., alias='vectorsdbCollections')
    vectorsdbdocuments: List[Metric] = Field(..., alias='vectorsdbDocuments')
    vectorsdbdatabasesstorage: List[Metric] = Field(..., alias='vectorsdbDatabasesStorage')
    vectorsdbdatabasesreads: List[Metric] = Field(..., alias='vectorsdbDatabasesReads')
    vectorsdbdatabaseswrites: List[Metric] = Field(..., alias='vectorsdbDatabasesWrites')
    embeddingstext: List[Metric] = Field(..., alias='embeddingsText')
    embeddingstexttokens: List[Metric] = Field(..., alias='embeddingsTextTokens')
    embeddingstextduration: List[Metric] = Field(..., alias='embeddingsTextDuration')
    embeddingstexterrors: List[Metric] = Field(..., alias='embeddingsTextErrors')
    embeddingstexttotal: float = Field(..., alias='embeddingsTextTotal')
    embeddingstexttokenstotal: float = Field(..., alias='embeddingsTextTokensTotal')
    embeddingstextdurationtotal: float = Field(..., alias='embeddingsTextDurationTotal')
    embeddingstexterrorstotal: float = Field(..., alias='embeddingsTextErrorsTotal')
    functionsexecutions: List[Metric] = Field(..., alias='functionsExecutions')
    functionsexecutionstotal: float = Field(..., alias='functionsExecutionsTotal')
    sitesexecutions: List[Metric] = Field(..., alias='sitesExecutions')
    sitesexecutionstotal: float = Field(..., alias='sitesExecutionsTotal')
    networktotal: float = Field(..., alias='networkTotal')
    backupsstoragetotal: float = Field(..., alias='backupsStorageTotal')
    screenshotsgenerated: List[Metric] = Field(..., alias='screenshotsGenerated')
    screenshotsgeneratedtotal: float = Field(..., alias='screenshotsGeneratedTotal')
    realtimeconnectionstotal: float = Field(..., alias='realtimeConnectionsTotal')
    realtimemessagestotal: float = Field(..., alias='realtimeMessagesTotal')
    realtimebandwidthtotal: float = Field(..., alias='realtimeBandwidthTotal')
    realtimeconnections: List[Metric] = Field(..., alias='realtimeConnections')
    realtimemessages: List[Metric] = Field(..., alias='realtimeMessages')
    realtimebandwidth: List[Metric] = Field(..., alias='realtimeBandwidth')
