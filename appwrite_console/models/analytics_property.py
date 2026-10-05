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
    timezone : str
        IANA timezone used to define the daily boundary for stats.
    enabled : bool
        Whether tracking is currently active.
    public : bool
        Whether stats for this property are publicly viewable.
    allowedorigins : List[Any]
        List of origins allowed to send tracking events. Use [&quot;*&quot;] to allow all.
    snippetid : str
        Unique identifier for the tracking script snippet.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    domain: str = Field(..., alias='domain')
    timezone: str = Field(..., alias='timezone')
    enabled: bool = Field(..., alias='enabled')
    public: bool = Field(..., alias='public')
    allowedorigins: List[Any] = Field(..., alias='allowedOrigins')
    snippetid: str = Field(..., alias='snippetId')
