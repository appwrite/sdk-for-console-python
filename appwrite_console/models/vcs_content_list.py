from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .vcs_content import VcsContent


class VcsContentList(AppwriteModel):
    """
    VCS Content List

    Attributes
    ----------
    total : float
        Total number of contents that matched your query.
    contents : List[VcsContent]
        List of contents.
    """

    total: float = Field(..., alias='total')
    contents: List[VcsContent] = Field(..., alias='contents')
