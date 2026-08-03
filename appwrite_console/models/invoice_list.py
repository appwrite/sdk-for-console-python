from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .invoice import Invoice

class InvoiceList(AppwriteModel):
    """
    Billing invoices list

    Attributes
    ----------
    total : float
        Total number of invoices that matched your query.
    invoices : List[Invoice]
        List of invoices.
    """
    total: float = Field(..., alias='total')
    invoices: List[Invoice] = Field(..., alias='invoices')
