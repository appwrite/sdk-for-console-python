from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .template_site import TemplateSite


class TemplateSiteList(AppwriteModel):
    """
    Site Templates List

    Attributes
    ----------
    total : float
        Total number of templates that matched your query.
    templates : List[TemplateSite]
        List of templates.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    templates: List[TemplateSite] = Field(
        ...,
        alias='templates',
    )
