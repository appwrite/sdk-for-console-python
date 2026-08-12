from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .console_o_auth2_provider import ConsoleOAuth2Provider

class ConsoleOAuth2ProviderList(AppwriteModel):
    """
    Console OAuth2 Providers List

    Attributes
    ----------
    total : float
        Total number of OAuth2 providers exposed by the server.
    oauth2providers : List[ConsoleOAuth2Provider]
        List of OAuth2 providers, each with the parameters required to configure it.
    """
    total: float = Field(..., alias='total')
    oauth2providers: List[ConsoleOAuth2Provider] = Field(..., alias='oAuth2Providers')
