from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .plan_change_project_compliance import PlanChangeProjectCompliance

class PlanChangeLimits(AppwriteModel):
    """
    PlanChangeLimits

    Attributes
    ----------
    totalprojects : float
        Total number of projects in the organization
    noncompliantprojects : float
        Number of projects exceeding target plan limits
    canchangeplan : bool
        Whether the plan change is allowed
    projects : List[PlanChangeProjectCompliance]
        Project compliance details
    unsupportedaddons : List[Any]
        Active addon keys that the target plan does not support. When non-empty, `canChangePlan` is false.
    """
    totalprojects: float = Field(..., alias='totalProjects')
    noncompliantprojects: float = Field(..., alias='nonCompliantProjects')
    canchangeplan: bool = Field(..., alias='canChangePlan')
    projects: List[PlanChangeProjectCompliance] = Field(..., alias='projects')
    unsupportedaddons: List[Any] = Field(..., alias='unsupportedAddons')
