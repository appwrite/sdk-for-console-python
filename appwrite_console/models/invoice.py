from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .usage_resources import UsageResources

class Invoice(AppwriteModel):
    """
    Invoice

    Attributes
    ----------
    id : str
        Invoice ID.
    createdat : str
        Invoice creation time in ISO 8601 format.
    updatedat : str
        Invoice update date in ISO 8601 format.
    permissions : List[Any]
        Invoice permissions. [Learn more about permissions](/docs/permissions).
    teamid : str
        Project ID
    aggregationid : str
        Aggregation ID
    plan : str
        Billing plan selected. Can be one of `tier-0`, `tier-1` or `tier-2`.
    usage : List[UsageResources]
        Usage breakdown per resource
    amount : float
        Invoice Amount
    tax : float
        Tax percentage
    taxamount : float
        Tax amount
    vat : float
        VAT percentage
    vatamount : float
        VAT amount
    grossamount : float
        Gross amount after vat, tax, and discounts applied.
    creditsused : float
        Credits used.
    currency : str
        Currency the invoice is in
    clientsecret : str
        Client secret for processing failed payments in front-end
    status : str
        Invoice status
    type : str
        Invoice type. Can be one of `subscription`, `domain_purchase`, `domain_renewal`, `domain_transfer`, or `addon_*`.
    lasterror : str
        Last payment error associated with the invoice
    dueat : str
        Invoice due date.
    xfrom : str
        Beginning date of the invoice
    to : str
        End date of the invoice
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    teamid: str = Field(..., alias='teamId')
    aggregationid: str = Field(..., alias='aggregationId')
    plan: str = Field(..., alias='plan')
    usage: List[UsageResources] = Field(..., alias='usage')
    amount: float = Field(..., alias='amount')
    tax: float = Field(..., alias='tax')
    taxamount: float = Field(..., alias='taxAmount')
    vat: float = Field(..., alias='vat')
    vatamount: float = Field(..., alias='vatAmount')
    grossamount: float = Field(..., alias='grossAmount')
    creditsused: float = Field(..., alias='creditsUsed')
    currency: str = Field(..., alias='currency')
    clientsecret: str = Field(..., alias='clientSecret')
    status: str = Field(..., alias='status')
    type: str = Field(..., alias='type')
    lasterror: str = Field(..., alias='lastError')
    dueat: str = Field(..., alias='dueAt')
    xfrom: str = Field(..., alias='from')
    to: str = Field(..., alias='to')
