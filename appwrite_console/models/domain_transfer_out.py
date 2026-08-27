from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DomainTransferOut(AppwriteModel):
    """
    domainTransferOut

    Attributes
    ----------
    authcode : str
        Domain transfer authorization code.
    """

    authcode: str = Field(..., alias='authCode')
