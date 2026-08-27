from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .affiliate_reward import AffiliateReward


class AffiliateRewardList(AppwriteModel):
    """
    Affiliate rewards list

    Attributes
    ----------
    total : float
        Total number of rewards that matched your query.
    rewards : List[AffiliateReward]
        List of rewards.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    rewards: List[AffiliateReward] = Field(
        ...,
        alias='rewards',
    )
