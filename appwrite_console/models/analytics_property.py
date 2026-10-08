from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class AnalyticsProperty(AppwriteModel):
    """
    AnalyticsProperty

    Attributes
    ----------
    id : str
        Analytics property ID.
    createdat : str
        Property creation date in ISO 8601 format.
    updatedat : str
        Property update date in ISO 8601 format.
    name : str
        Human-readable name of the tracked website or application.
    domain : str
        Primary domain being tracked (e.g. example.com). May be empty for native apps.
    enabled : bool
        Whether tracking is currently active.
    public : bool
        Whether stats for this property are publicly viewable.
    allowedorigins : List[Any]
        List of origins allowed to send tracking events. Use [&quot;*&quot;] to allow all.
    accessedat : str
        Most recent event date in ISO 8601 format. This attribute is only updated again after 24 hours.
    firstaccessedat : str
        First event date in ISO 8601 format. Empty until the property receives its first event.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    domain: str = Field(..., alias='domain')
    enabled: bool = Field(..., alias='enabled')
    public: bool = Field(..., alias='public')
    allowedorigins: List[Any] = Field(..., alias='allowedOrigins')
    accessedat: str = Field(..., alias='accessedAt')
    firstaccessedat: str = Field(..., alias='firstAccessedAt')
