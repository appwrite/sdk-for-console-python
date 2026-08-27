from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .vcs_namespace import VcsNamespace


class VcsNamespaceList(AppwriteModel):
    """
    VCS Namespaces List

    Attributes
    ----------
    total : float
        Total number of namespaces that matched your query.
    namespaces : List[VcsNamespace]
        List of namespaces.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    namespaces: List[VcsNamespace] = Field(
        ...,
        alias='namespaces',
    )
