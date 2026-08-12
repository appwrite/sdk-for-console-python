from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .plan_change_estimation_details import PlanChangeEstimationDetails
from .plan_change_limits import PlanChangeLimits

class EstimationPlanChange(AppwriteModel):
    """
    EstimationPlanChange

    Attributes
    ----------
    currentbillingplanid : str
        Current billing plan ID
    targetbillingplanid : str
        Target billing plan ID
    direction : str
        Direction of plan change: upgrade, downgrade, or same
    estimation : PlanChangeEstimationDetails
        Cost estimation details
    limits : PlanChangeLimits
        Plan limits and compliance information
    """
    currentbillingplanid: str = Field(..., alias='currentBillingPlanId')
    targetbillingplanid: str = Field(..., alias='targetBillingPlanId')
    direction: str = Field(..., alias='direction')
    estimation: PlanChangeEstimationDetails = Field(..., alias='estimation')
    limits: PlanChangeLimits = Field(..., alias='limits')
