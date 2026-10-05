from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class AnalyticsMetric(AppwriteModel):
    """
    AnalyticsMetric

    Attributes
    ----------
    value : Optional[str]
        Dimension value this row covers. Null when no dimension was requested, empty when the dimension could not be derived for those events.
    date : Optional[str]
        Start of the time bucket this row covers, in ISO 8601. Null when no interval was requested.
    visitors : float
        Unique visitors in the requested range.
    sessions : float
        Unique sessions in the requested range.
    pageviews : Optional[float]
        Total pageview events (events with name=&quot;pageview&quot;) in the requested range. Only the flat aggregate computes it; null on breakdown and time-series rows.
    events : float
        Total events in the requested range.
    visits : Optional[float]
        Total sessions with activity in the requested range. Only the flat aggregate computes it; null on breakdown and time-series rows.
    bouncerate : Optional[float]
        Share of single-event sessions, as a percentage. Only the flat aggregate computes it; null on breakdown and time-series rows.
    visitduration : Optional[float]
        Average session length in seconds, measured first event to last event. Single-event sessions count as 0. Only the flat aggregate computes it; null on breakdown and time-series rows.
    viewspervisit : Optional[float]
        Average pageviews per session (pageviews divided by visits). Only the flat aggregate computes it; null on breakdown and time-series rows.
    scrolldepth : Optional[float]
        Average scroll depth across events, as a percentage. Only the flat aggregate computes it; null on breakdown and time-series rows.
    engagementtime : Optional[float]
        Average engaged time per session in seconds, counting only foreground time. Sessions that reported no engagement are excluded. Only the flat aggregate computes it; null on breakdown and time-series rows.
    """

    value: Optional[str] = Field(default=None, alias='value')
    date: Optional[str] = Field(default=None, alias='date')
    visitors: float = Field(..., alias='visitors')
    sessions: float = Field(..., alias='sessions')
    pageviews: Optional[float] = Field(default=None, alias='pageviews')
    events: float = Field(..., alias='events')
    visits: Optional[float] = Field(default=None, alias='visits')
    bouncerate: Optional[float] = Field(default=None, alias='bounceRate')
    visitduration: Optional[float] = Field(default=None, alias='visitDuration')
    viewspervisit: Optional[float] = Field(default=None, alias='viewsPerVisit')
    scrolldepth: Optional[float] = Field(default=None, alias='scrollDepth')
    engagementtime: Optional[float] = Field(default=None, alias='engagementTime')
