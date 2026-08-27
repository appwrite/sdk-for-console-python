from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class AffiliateReferral(AppwriteModel):
    """
    AffiliateReferral

    Attributes
    ----------
    id : str
        Referral ID.
    createdat : str
        Referral creation date in ISO 8601 format.
    updatedat : str
        Referral update date in ISO 8601 format.
    linkid : str
        Affiliate link ID used for attribution.
    referredusermaskedid : str
        Privacy-safe truncated referred user ID.
    referredusercountry : str
        ISO 3166-1 alpha-2 country code of the referred user at signup, when available.
    status : str
        Referral status. Can be one of `pending`, `converted`, or `expired`. `expired` is derived from `expiresAt` when still pending.
    attributedat : str
        Attribution time in ISO 8601 format.
    expiresat : str
        Attribution expiry time in ISO 8601 format.
    convertedat : Optional[str]
        Conversion time in ISO 8601 format.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    linkid: str = Field(..., alias='linkId')
    referredusermaskedid: str = Field(..., alias='referredUserMaskedId')
    referredusercountry: str = Field(..., alias='referredUserCountry')
    status: str = Field(..., alias='status')
    attributedat: str = Field(..., alias='attributedAt')
    expiresat: str = Field(..., alias='expiresAt')
    convertedat: Optional[str] = Field(default=None, alias='convertedAt')
