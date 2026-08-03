from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .provider_repository_framework import ProviderRepositoryFramework

class ProviderRepositoryFrameworkList(AppwriteModel):
    """
    Framework Provider Repositories List

    Attributes
    ----------
    total : float
        Total number of frameworkProviderRepositories that matched your query.
    frameworkproviderrepositories : List[ProviderRepositoryFramework]
        List of frameworkProviderRepositories.
    type : str
        Provider repository list type.
    """
    total: float = Field(..., alias='total')
    frameworkproviderrepositories: List[ProviderRepositoryFramework] = Field(..., alias='frameworkProviderRepositories')
    type: str = Field(..., alias='type')
