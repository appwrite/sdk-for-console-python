from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .console_o_auth2_provider_parameter import ConsoleOAuth2ProviderParameter

class ConsoleOAuth2Provider(AppwriteModel):
    """
    Console OAuth2 Provider

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    parameters : List[ConsoleOAuth2ProviderParameter]
        List of parameters required to configure this OAuth2 provider.
    """
    id: str = Field(..., alias='$id')
    parameters: List[ConsoleOAuth2ProviderParameter] = Field(..., alias='parameters')
