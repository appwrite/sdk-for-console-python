from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .affiliate_link import AffiliateLink


class AffiliateLinkList(AppwriteModel):
    """
    Affiliate links list

    Attributes
    ----------
    total : float
        Total number of links that matched your query.
    links : List[AffiliateLink]
        List of links.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    links: List[AffiliateLink] = Field(
        ...,
        alias='links',
    )
