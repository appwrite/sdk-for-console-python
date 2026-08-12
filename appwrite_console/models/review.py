from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Review(AppwriteModel):
    """
    Review

    Attributes
    ----------
    name : str
        Name of user
    image : str
        Reviewer image
    description : str
        Reviewer description
    review : str
        Review
    """
    name: str = Field(..., alias='name')
    image: str = Field(..., alias='image')
    description: str = Field(..., alias='description')
    review: str = Field(..., alias='review')
