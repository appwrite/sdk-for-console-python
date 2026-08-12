from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class UsageDataPoint(AppwriteModel):
    """
    usageDataPoint

    Attributes
    ----------
    time : str
        Bucket start timestamp (ISO 8601). When `interval` is omitted this is the request end time, marking the aggregate as-of moment.
    value : float
        Aggregated value for the bucket. Counters are whole numbers; gauge rates (e.g. queries per second) may be fractional.
    path : Optional[str]
        API endpoint path when broken down by `path`.
    method : Optional[str]
        HTTP method when broken down by `method`.
    status : Optional[str]
        HTTP status code when broken down by `status`.
    service : Optional[str]
        API service segment when broken down by `service`.
    country : Optional[str]
        Country code when broken down by `country`.
    continentcode : Optional[str]
        Continent code when broken down by `continentCode`.
    city : Optional[str]
        City name when broken down by `city`.
    subdivisions : Optional[str]
        Region/state chain when broken down by `subdivisions`.
    isp : Optional[str]
        Internet service provider when broken down by `isp`.
    autonomoussystemnumber : Optional[str]
        Autonomous System Number (ASN) when broken down by `autonomousSystemNumber`.
    autonomoussystemorganization : Optional[str]
        Organization owning the ASN when broken down by `autonomousSystemOrganization`.
    connectiontype : Optional[str]
        Connection type (e.g. cable, cellular, corporate) when broken down by `connectionType`.
    connectionusagetype : Optional[str]
        User type (e.g. residential, business, hosting) when broken down by `connectionUsageType`.
    connectionorganization : Optional[str]
        Registered organization of the IP when broken down by `connectionOrganization`.
    region : Optional[str]
        Appwrite region when broken down by `region`.
    hostname : Optional[str]
        Caller origin hostname when broken down by `hostname`.
    ip : Optional[str]
        Caller IP address when broken down by `ip`.
    osname : Optional[str]
        Operating system name when broken down by `osName`.
    clienttype : Optional[str]
        Client type when broken down by `clientType`.
    clientname : Optional[str]
        Client name when broken down by `clientName`.
    sdk : Optional[str]
        SDK name when broken down by `sdk`.
    sdkversion : Optional[str]
        SDK version when broken down by `sdkVersion`.
    devicename : Optional[str]
        Device classification when broken down by `deviceName`.
    teamid : Optional[str]
        Owning team ID when broken down by `teamId`.
    resourceid : Optional[str]
        External resource ID when broken down by `resourceId`.
    resourcetype : Optional[str]
        Resource type when broken down by `resourceType`.
    ordinal : Optional[str]
        Node ordinal when broken down by `ordinal`. A stable per-node identity, not a role: ordinal 0 is the first member created, and a failover can leave the primary on any ordinal. Read the role from the database&#039;s replicas endpoint.
    """
    time: str = Field(..., alias='time')
    value: float = Field(..., alias='value')
    path: Optional[str] = Field(default=None, alias='path')
    method: Optional[str] = Field(default=None, alias='method')
    status: Optional[str] = Field(default=None, alias='status')
    service: Optional[str] = Field(default=None, alias='service')
    country: Optional[str] = Field(default=None, alias='country')
    continentcode: Optional[str] = Field(default=None, alias='continentCode')
    city: Optional[str] = Field(default=None, alias='city')
    subdivisions: Optional[str] = Field(default=None, alias='subdivisions')
    isp: Optional[str] = Field(default=None, alias='isp')
    autonomoussystemnumber: Optional[str] = Field(default=None, alias='autonomousSystemNumber')
    autonomoussystemorganization: Optional[str] = Field(default=None, alias='autonomousSystemOrganization')
    connectiontype: Optional[str] = Field(default=None, alias='connectionType')
    connectionusagetype: Optional[str] = Field(default=None, alias='connectionUsageType')
    connectionorganization: Optional[str] = Field(default=None, alias='connectionOrganization')
    region: Optional[str] = Field(default=None, alias='region')
    hostname: Optional[str] = Field(default=None, alias='hostname')
    ip: Optional[str] = Field(default=None, alias='ip')
    osname: Optional[str] = Field(default=None, alias='osName')
    clienttype: Optional[str] = Field(default=None, alias='clientType')
    clientname: Optional[str] = Field(default=None, alias='clientName')
    sdk: Optional[str] = Field(default=None, alias='sdk')
    sdkversion: Optional[str] = Field(default=None, alias='sdkVersion')
    devicename: Optional[str] = Field(default=None, alias='deviceName')
    teamid: Optional[str] = Field(default=None, alias='teamId')
    resourceid: Optional[str] = Field(default=None, alias='resourceId')
    resourcetype: Optional[str] = Field(default=None, alias='resourceType')
    ordinal: Optional[str] = Field(default=None, alias='ordinal')
