from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .organization import Organization

T = TypeVar('T')


class OrganizationList(AppwriteModel, Generic[T]):
    """
    Organizations list

    Attributes
    ----------
    total : float
        Total number of teams that matched your query.
    teams : List[Organization[T]]
        List of teams.
    """

    total: float = Field(
        ...,
        alias='total',
    )
    teams: List[Organization[T]] = Field(
        ...,
        alias='teams',
    )

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'OrganizationList[T]':
        """Create OrganizationList instance with typed data."""
        instance = cls.model_validate(data)
        if 'teams' in data and data['teams'] is not None:
            instance.teams = [Organization.with_data(row, model_type) for row in data['teams']]
        return instance
