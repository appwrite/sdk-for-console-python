from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .console_key_scope import ConsoleKeyScope


class ConsoleKeyScopeList(AppwriteModel):
    """
    Console Key Scopes List

    Attributes
    ----------
    total : float
        Total number of key scopes exposed by the server.
    scopes : List[ConsoleKeyScope]
        List of key scopes, each with its ID and description.
    """

    total: float = Field(..., alias='total')
    scopes: List[ConsoleKeyScope] = Field(..., alias='scopes')
