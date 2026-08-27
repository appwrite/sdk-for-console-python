from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .plan_change_resource_compliance import PlanChangeResourceCompliance
from .plan_change_project_compliance import PlanChangeProjectCompliance


class PlanChangeLimits(AppwriteModel):
    """
    PlanChangeLimits

    Attributes
    ----------
    canchangeplan : bool
        Whether the plan change is allowed
    unsupportedaddons : List[Any]
        Active addon keys that the target plan does not support. When non-empty, `canChangePlan` is false.
    projects : PlanChangeResourceCompliance
        Project count against the target plan limit
    members : PlanChangeResourceCompliance
        Organization member count against the target plan limit
    domains : PlanChangeResourceCompliance
        Custom domain count against the target plan limit
    noncompliantprojects : float
        Number of projects exceeding target plan limits
    projectcompliance : List[PlanChangeProjectCompliance]
        Per-project compliance details. Populated for downgrades only.
    """

    canchangeplan: bool = Field(
        ...,
        alias='canChangePlan',
    )
    unsupportedaddons: List[Any] = Field(
        ...,
        alias='unsupportedAddons',
    )
    projects: PlanChangeResourceCompliance = Field(
        ...,
        alias='projects',
    )
    members: PlanChangeResourceCompliance = Field(
        ...,
        alias='members',
    )
    domains: PlanChangeResourceCompliance = Field(
        ...,
        alias='domains',
    )
    noncompliantprojects: float = Field(
        ...,
        alias='nonCompliantProjects',
    )
    projectcompliance: List[PlanChangeProjectCompliance] = Field(
        ...,
        alias='projectCompliance',
    )
