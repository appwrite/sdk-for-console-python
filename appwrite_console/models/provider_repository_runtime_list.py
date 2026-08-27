from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .provider_repository_runtime import ProviderRepositoryRuntime


class ProviderRepositoryRuntimeList(AppwriteModel):
    """
    Runtime Provider Repositories List

    Attributes
    ----------
    total : float
        Total number of runtimeProviderRepositories that matched your query.
    runtimeproviderrepositories : List[ProviderRepositoryRuntime]
        List of runtimeProviderRepositories.
    type : str
        Provider repository list type.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    runtimeproviderrepositories: List[ProviderRepositoryRuntime] = Field(
        ...,
        alias='runtimeProviderRepositories',
    )
    type: str = Field(
        ...,
        alias='type',
    )
