from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .waf_rule import WafRule


class WafRuleList(AppwriteModel):
    """
    WAF rule list

    Attributes
    ----------
    total : float
        Total number of rules that matched your query.
    rules : List[WafRule]
        List of rules.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    rules: List[WafRule] = Field(
        ...,
        alias='rules',
    )
