from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .aggregation_breakdown import AggregationBreakdown
from .usage_resources import UsageResources

class AggregationTeam(AppwriteModel):
    """
    Team

    Attributes
    ----------
    id : str
        Aggregation ID.
    createdat : str
        Aggregation creation time in ISO 8601 format.
    updatedat : str
        Aggregation update date in ISO 8601 format.
    permissions : List[Any]
        Aggregation permissions. [Learn more about permissions](/docs/permissions).
    xfrom : str
        Beginning date of the invoice
    to : str
        End date of the invoice
    usagestorage : float
        Total storage usage
    usagetotalstorage : float
        Total storage usage with builds storage
    usagefilesstorage : float
        Total files storage usage
    usagedeploymentsstorage : float
        Total deployments storage usage
    usagebuildsstorage : float
        Total builds storage usage
    usagedatabasesstorage : float
        Total databases storage usage
    usageusers : float
        Total active users for the billing period
    usageexecutions : float
        Total number of executions for the billing period
    usagebandwidth : float
        Total bandwidth usage for the billing period
    usagerealtime : float
        Peak concurrent realtime connections for the billing period
    usagerealtimemessages : float
        Total realtime messages sent for the billing period
    usagerealtimebandwidth : float
        Total realtime bandwidth usage for the billing period
    additionalmembers : float
        Additional members
    additionalmemberamount : float
        Additional members cost
    additionalstorageamount : float
        Additional storage usage cost
    additionalusersamount : float
        Additional users usage cost.
    additionalexecutionsamount : float
        Additional executions usage cost
    additionalbandwidthamount : float
        Additional bandwidth usage cost
    additionalrealtimeamount : float
        Additional realtime usage cost
    plan : str
        Billing plan
    amount : float
        Aggregated amount
    breakdown : List[AggregationBreakdown]
        Aggregation project breakdown
    resources : List[UsageResources]
        Usage resources
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    xfrom: str = Field(..., alias='from')
    to: str = Field(..., alias='to')
    usagestorage: float = Field(..., alias='usageStorage')
    usagetotalstorage: float = Field(..., alias='usageTotalStorage')
    usagefilesstorage: float = Field(..., alias='usageFilesStorage')
    usagedeploymentsstorage: float = Field(..., alias='usageDeploymentsStorage')
    usagebuildsstorage: float = Field(..., alias='usageBuildsStorage')
    usagedatabasesstorage: float = Field(..., alias='usageDatabasesStorage')
    usageusers: float = Field(..., alias='usageUsers')
    usageexecutions: float = Field(..., alias='usageExecutions')
    usagebandwidth: float = Field(..., alias='usageBandwidth')
    usagerealtime: float = Field(..., alias='usageRealtime')
    usagerealtimemessages: float = Field(..., alias='usageRealtimeMessages')
    usagerealtimebandwidth: float = Field(..., alias='usageRealtimeBandwidth')
    additionalmembers: float = Field(..., alias='additionalMembers')
    additionalmemberamount: float = Field(..., alias='additionalMemberAmount')
    additionalstorageamount: float = Field(..., alias='additionalStorageAmount')
    additionalusersamount: float = Field(..., alias='additionalUsersAmount')
    additionalexecutionsamount: float = Field(..., alias='additionalExecutionsAmount')
    additionalbandwidthamount: float = Field(..., alias='additionalBandwidthAmount')
    additionalrealtimeamount: float = Field(..., alias='additionalRealtimeAmount')
    plan: str = Field(..., alias='plan')
    amount: float = Field(..., alias='amount')
    breakdown: List[AggregationBreakdown] = Field(..., alias='breakdown')
    resources: List[UsageResources] = Field(..., alias='resources')
