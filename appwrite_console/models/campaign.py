from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .review import Review

class Campaign(AppwriteModel):
    """
    Campaign

    Attributes
    ----------
    id : str
        Campaign ID
    template : str
        Campaign template
    title : str
        Campaign title
    description : str
        Campaign description
    plan : Optional[str]
        Billing plan campaign is associated with
    cta : Optional[str]
        Campaign CTA
    claimed : Optional[str]
        Campaign info when claimed
    unclaimed : Optional[str]
        Campaign infor when unclaimed
    image : Optional[Dict[str, Any]]
        Campaign images
    reviews : Optional[List[Review]]
        Campaign reviews
    onlyneworgs : Optional[bool]
        Campaign valid only for new orgs.
    footer : Optional[bool]
        Is footer
    """
    id: str = Field(..., alias='$id')
    template: str = Field(..., alias='template')
    title: str = Field(..., alias='title')
    description: str = Field(..., alias='description')
    plan: Optional[str] = Field(default=None, alias='plan')
    cta: Optional[str] = Field(default=None, alias='cta')
    claimed: Optional[str] = Field(default=None, alias='claimed')
    unclaimed: Optional[str] = Field(default=None, alias='unclaimed')
    image: Optional[Dict[str, Any]] = Field(default=None, alias='image')
    reviews: Optional[List[Review]] = Field(default=None, alias='reviews')
    onlyneworgs: Optional[bool] = Field(default=None, alias='onlyNewOrgs')
    footer: Optional[bool] = Field(default=None, alias='footer')
