from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .affiliate_referral import AffiliateReferral

class AffiliateReferralList(AppwriteModel):
    """
    Affiliate referrals list

    Attributes
    ----------
    total : float
        Total number of referrals that matched your query.
    referrals : List[AffiliateReferral]
        List of referrals.
    """
    total: float = Field(..., alias='total')
    referrals: List[AffiliateReferral] = Field(..., alias='referrals')
