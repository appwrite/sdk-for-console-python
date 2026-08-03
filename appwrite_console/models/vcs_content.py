from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class VcsContent(AppwriteModel):
    """
    VcsContents

    Attributes
    ----------
    size : Optional[float]
        Content size in bytes. Only files have size, and for directories, 0 is returned.
    isdirectory : Optional[bool]
        If a content is a directory. Directories can be used to check nested contents.
    name : str
        Name of directory or file.
    """
    size: Optional[float] = Field(default=None, alias='size')
    isdirectory: Optional[bool] = Field(default=None, alias='isDirectory')
    name: str = Field(..., alias='name')
