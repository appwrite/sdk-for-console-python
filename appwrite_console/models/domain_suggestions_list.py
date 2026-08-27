from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .domain_suggestion import DomainSuggestion


class DomainSuggestionsList(AppwriteModel):
    """
    Domain suggestions list

    Attributes
    ----------
    total : float
        Total number of suggestions that matched your query.
    suggestions : List[DomainSuggestion]
        List of suggestions.
    """

    total: float = Field(..., alias='total')
    suggestions: List[DomainSuggestion] = Field(..., alias='suggestions')
