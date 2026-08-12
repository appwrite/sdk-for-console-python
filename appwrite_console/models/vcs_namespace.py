from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class VcsNamespace(AppwriteModel):
    """
    VcsNamespace

    Attributes
    ----------
    id : str
        VCS (Version Control System) namespace ID.
    name : str
        VCS (Version Control System) namespace display name.
    path : str
        VCS (Version Control System) namespace path, used to filter repositories by namespace.
    type : str
        Namespace type. Either the user&#039;s personal namespace or a group/organization.
    avatarurl : str
        Namespace avatar URL.
    """
    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    path: str = Field(..., alias='path')
    type: str = Field(..., alias='type')
    avatarurl: str = Field(..., alias='avatarUrl')
