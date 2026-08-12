from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel
from .template_framework import TemplateFramework
from .template_variable import TemplateVariable

class TemplateSite(AppwriteModel):
    """
    Template Site

    Attributes
    ----------
    key : str
        Site Template ID.
    name : str
        Site Template Name.
    tagline : str
        Short description of template
    demourl : str
        URL hosting a template demo.
    screenshotdark : str
        File URL with preview screenshot in dark theme preference.
    screenshotlight : str
        File URL with preview screenshot in light theme preference.
    usecases : List[Any]
        Site use cases.
    frameworks : List[TemplateFramework]
        List of frameworks that can be used with this template.
    vcsprovider : str
        VCS (Version Control System) Provider.
    providerrepositoryid : str
        VCS (Version Control System) Repository ID
    providerowner : str
        VCS (Version Control System) Owner.
    providerversion : str
        VCS (Version Control System) branch version (tag).
    variables : List[TemplateVariable]
        Site variables.
    """
    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    tagline: str = Field(..., alias='tagline')
    demourl: str = Field(..., alias='demoUrl')
    screenshotdark: str = Field(..., alias='screenshotDark')
    screenshotlight: str = Field(..., alias='screenshotLight')
    usecases: List[Any] = Field(..., alias='useCases')
    frameworks: List[TemplateFramework] = Field(..., alias='frameworks')
    vcsprovider: str = Field(..., alias='vcsProvider')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerowner: str = Field(..., alias='providerOwner')
    providerversion: str = Field(..., alias='providerVersion')
    variables: List[TemplateVariable] = Field(..., alias='variables')
