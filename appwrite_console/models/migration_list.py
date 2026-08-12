from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .migration import Migration

class MigrationList(AppwriteModel):
    """
    Migrations List

    Attributes
    ----------
    total : float
        Total number of migrations that matched your query.
    migrations : List[Migration]
        List of migrations.
    """
    total: float = Field(..., alias='total')
    migrations: List[Migration] = Field(..., alias='migrations')
