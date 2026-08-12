from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .postgres_extension import PostgresExtension

class PostgresExtensionList(AppwriteModel):
    """
    Postgres extensions list

    Attributes
    ----------
    total : float
        Total number of extensions that matched your query.
    extensions : List[PostgresExtension]
        List of extensions.
    """
    total: float = Field(..., alias='total')
    extensions: List[PostgresExtension] = Field(..., alias='extensions')
