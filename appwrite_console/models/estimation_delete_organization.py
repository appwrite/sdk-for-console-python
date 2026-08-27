from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .invoice import Invoice


class EstimationDeleteOrganization(AppwriteModel):
    """
    DeleteOrganization

    Attributes
    ----------
    unpaidinvoices : List[Invoice]
        List of unpaid invoices
    """

    unpaidinvoices: List[Invoice] = Field(
        ...,
        alias='unpaidInvoices',
    )
