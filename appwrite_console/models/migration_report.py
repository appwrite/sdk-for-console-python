from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MigrationReport(AppwriteModel):
    """
    Migration Report

    Attributes
    ----------
    user : float
        Number of users to be migrated.
    team : float
        Number of teams to be migrated.
    database : float
        Number of databases to be migrated.
    row : float
        Number of rows to be migrated.
    file : float
        Number of files to be migrated.
    bucket : float
        Number of buckets to be migrated.
    function : float
        Number of functions to be migrated.
    platform : float
        Number of platforms to be migrated.
    api_key : float
        Number of API keys to be migrated.
    project_variable : float
        Number of project variables to be migrated.
    webhook : float
        Number of webhooks to be migrated.
    auth_methods : float
        Number of auth-method configs to be migrated (always 0 or 1 — the project-level flag bundle).
    project_protocols : float
        Number of protocol configs to be migrated (always 0 or 1 — the project-level REST/GraphQL/WebSocket flags).
    project_labels : float
        Number of label sets to be migrated (always 0 or 1 — the project-level RBAC label array).
    project_services : float
        Number of service configs to be migrated (always 0 or 1 — the project-level enable/disable flags for all 17 services).
    policies : float
        Number of policy bundles to be migrated (always 0 or 1 — the project-level security policies covering password rules, session behavior, user limits, and membership privacy).
    smtp : float
        Number of SMTP configurations to be migrated (always 0 or 1 — the project-level custom SMTP settings; password is not exposed by the source API).
    rule : float
        Number of custom-domain proxy rules to be migrated. Auto-generated `.appwrite.network` rules are skipped — they are recreated by parent Function/Site migration.
    project_email_template : float
        Number of custom email templates to be migrated (one per templateId × locale pair).
    site : float
        Number of sites to be migrated.
    provider : float
        Number of providers to be migrated.
    topic : float
        Number of topics to be migrated.
    subscriber : float
        Number of subscribers to be migrated.
    message : float
        Number of messages to be migrated.
    size : float
        Size of files to be migrated in mb.
    version : str
        Version of the Appwrite instance to be migrated.
    oauth2_provider : float
        Number of OAuth2 provider configurations to be migrated. Secrets (clientSecret, p8File) are never migrated — destination admin must re-enter them per provider.
    backup_policy : float
        Number of backup policies to be migrated.
    """
    user: float = Field(..., alias='user')
    team: float = Field(..., alias='team')
    database: float = Field(..., alias='database')
    row: float = Field(..., alias='row')
    file: float = Field(..., alias='file')
    bucket: float = Field(..., alias='bucket')
    function: float = Field(..., alias='function')
    platform: float = Field(..., alias='platform')
    api_key: float = Field(..., alias='api-key')
    project_variable: float = Field(..., alias='project-variable')
    webhook: float = Field(..., alias='webhook')
    auth_methods: float = Field(..., alias='auth-methods')
    project_protocols: float = Field(..., alias='project-protocols')
    project_labels: float = Field(..., alias='project-labels')
    project_services: float = Field(..., alias='project-services')
    policies: float = Field(..., alias='policies')
    smtp: float = Field(..., alias='smtp')
    rule: float = Field(..., alias='rule')
    project_email_template: float = Field(..., alias='project-email-template')
    site: float = Field(..., alias='site')
    provider: float = Field(..., alias='provider')
    topic: float = Field(..., alias='topic')
    subscriber: float = Field(..., alias='subscriber')
    message: float = Field(..., alias='message')
    size: float = Field(..., alias='size')
    version: str = Field(..., alias='version')
    oauth2_provider: float = Field(..., alias='oauth2-provider')
    backup_policy: float = Field(..., alias='backup-policy')
