from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .notification import Notification

class NotificationList(AppwriteModel):
    """
    Notifications List

    Attributes
    ----------
    total : float
        Total number of notifications that matched your query.
    notifications : List[Notification]
        List of notifications.
    """
    total: float = Field(..., alias='total')
    notifications: List[Notification] = Field(..., alias='notifications')
