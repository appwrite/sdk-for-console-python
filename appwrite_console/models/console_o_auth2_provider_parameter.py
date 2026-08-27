from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class ConsoleOAuth2ProviderParameter(AppwriteModel):
    """
    Console OAuth2 Provider Parameter

    Attributes
    ----------
    id : str
        Parameter ID. Maps to the request body field used by the project OAuth2 update endpoint (e.g. `clientId`, `appKey`, `tenant`).
    name : str
        Verbose, user-facing parameter name as shown in the provider&#039;s own dashboard. Includes alternate names when the provider exposes more than one.
    example : str
        Example value for this parameter.
    hint : str
        Optional hint for this parameter, typically calling out a common wrong value. Empty string when no hint is set.
    """

    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    example: str = Field(..., alias='example')
    hint: str = Field(..., alias='hint')
