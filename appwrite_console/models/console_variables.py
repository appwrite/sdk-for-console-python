from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr
from .base_model import AppwriteModel

class ConsoleVariables(AppwriteModel):
    """
    Console Variables

    Attributes
    ----------
    app_domain_target_cname : str
        CNAME target for your Appwrite custom domains.
    app_domain_target_a : str
        A target for your Appwrite custom domains.
    app_compute_build_timeout : float
        Maximum build timeout in seconds.
    app_domain_target_aaaa : str
        AAAA target for your Appwrite custom domains.
    app_domain_target_caa : str
        CAA target for your Appwrite custom domains.
    app_storage_limit : float
        Maximum file size allowed for file upload in bytes.
    app_compute_size_limit : float
        Maximum file size allowed for deployment in bytes.
    app_usage_stats : str
        Defines if usage stats are enabled. This value is set to &#039;enabled&#039; by default, to disable the usage stats set the value to &#039;disabled&#039;.
    app_vcs_enabled : bool
        Defines if VCS (Version Control System) is enabled.
    app_vcs_providers : List[Any]
        List of configured VCS providers.
    app_domain_enabled : bool
        Defines if main domain is configured. If so, custom domains can be created.
    app_assistant_enabled : bool
        Defines if AI assistant is enabled.
    app_domain_sites : str
        A comma separated list of domains to use for site URLs.
    app_domain_functions : str
        A domain to use for function URLs.
    app_options_force_https : str
        Defines if HTTPS is enforced for all requests.
    app_domains_nameservers : str
        Comma-separated list of nameservers.
    app_db_adapter : str
        Database adapter in use.
    supportforrelationships : bool
        Whether the database adapter supports relationships.
    supportforoperators : bool
        Whether the database adapter supports operators.
    supportforspatials : bool
        Whether the database adapter supports spatial attributes.
    supportforspatialindexnull : bool
        Whether the database adapter supports spatial indexes on nullable columns.
    supportforfulltextwildcard : bool
        Whether the database adapter supports fulltext wildcard search.
    supportformultiplefulltextindexes : bool
        Whether the database adapter supports multiple fulltext indexes per collection.
    supportforattributeresizing : bool
        Whether the database adapter supports resizing attributes.
    supportforschemas : bool
        Whether the database adapter supports fixed schemas with row width limits.
    maxindexlength : float
        Maximum index length supported by the database adapter.
    supportforintegerids : bool
        Whether the database adapter uses integer sequence IDs.
    app_console_email_verification : str
        Whether email verification for console users is required. Can be &quot;true&quot; or &quot;false&quot;.
    """
    app_domain_target_cname: str = Field(..., alias='_APP_DOMAIN_TARGET_CNAME')
    app_domain_target_a: str = Field(..., alias='_APP_DOMAIN_TARGET_A')
    app_compute_build_timeout: float = Field(..., alias='_APP_COMPUTE_BUILD_TIMEOUT')
    app_domain_target_aaaa: str = Field(..., alias='_APP_DOMAIN_TARGET_AAAA')
    app_domain_target_caa: str = Field(..., alias='_APP_DOMAIN_TARGET_CAA')
    app_storage_limit: float = Field(..., alias='_APP_STORAGE_LIMIT')
    app_compute_size_limit: float = Field(..., alias='_APP_COMPUTE_SIZE_LIMIT')
    app_usage_stats: str = Field(..., alias='_APP_USAGE_STATS')
    app_vcs_enabled: bool = Field(..., alias='_APP_VCS_ENABLED')
    app_vcs_providers: List[Any] = Field(..., alias='_APP_VCS_PROVIDERS')
    app_domain_enabled: bool = Field(..., alias='_APP_DOMAIN_ENABLED')
    app_assistant_enabled: bool = Field(..., alias='_APP_ASSISTANT_ENABLED')
    app_domain_sites: str = Field(..., alias='_APP_DOMAIN_SITES')
    app_domain_functions: str = Field(..., alias='_APP_DOMAIN_FUNCTIONS')
    app_options_force_https: str = Field(..., alias='_APP_OPTIONS_FORCE_HTTPS')
    app_domains_nameservers: str = Field(..., alias='_APP_DOMAINS_NAMESERVERS')
    app_db_adapter: str = Field(..., alias='_APP_DB_ADAPTER')
    supportforrelationships: bool = Field(..., alias='supportForRelationships')
    supportforoperators: bool = Field(..., alias='supportForOperators')
    supportforspatials: bool = Field(..., alias='supportForSpatials')
    supportforspatialindexnull: bool = Field(..., alias='supportForSpatialIndexNull')
    supportforfulltextwildcard: bool = Field(..., alias='supportForFulltextWildcard')
    supportformultiplefulltextindexes: bool = Field(..., alias='supportForMultipleFulltextIndexes')
    supportforattributeresizing: bool = Field(..., alias='supportForAttributeResizing')
    supportforschemas: bool = Field(..., alias='supportForSchemas')
    maxindexlength: float = Field(..., alias='maxIndexLength')
    supportforintegerids: bool = Field(..., alias='supportForIntegerIds')
    app_console_email_verification: str = Field(..., alias='_APP_CONSOLE_EMAIL_VERIFICATION')
