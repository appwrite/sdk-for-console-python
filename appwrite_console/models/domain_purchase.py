from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from ..enums.domain_purchase_status import DomainPurchaseStatus

class DomainPurchase(AppwriteModel):
    """
    DomainPurchase

    Attributes
    ----------
    id : str
        Purchase/invoice ID.
    createdat : str
        Purchase creation time in ISO 8601 format.
    updatedat : str
        Purchase update date in ISO 8601 format.
    domainid : str
        Domain document ID.
    domain : str
        Domain name.
    organizationid : str
        Team ID that owns the domain.
    status : DomainPurchaseStatus
        Domain purchase status.
    clientsecret : str
        Stripe client secret for 3DS; empty when not applicable.
    amount : float
        Purchase amount.
    currency : str
        Currency code.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    domainid: str = Field(..., alias='domainId')
    domain: str = Field(..., alias='domain')
    organizationid: str = Field(..., alias='organizationId')
    status: DomainPurchaseStatus = Field(..., alias='status')
    clientsecret: str = Field(..., alias='clientSecret')
    amount: float = Field(..., alias='amount')
    currency: str = Field(..., alias='currency')
