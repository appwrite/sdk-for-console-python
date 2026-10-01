# Change Log

## 0.7.0

* Breaking: Removed `account.list_logs`, `teams.list_logs`, `users.list_logs` and the `Log`/`LogList` models
* Breaking: Removed dev keys: `projects.*_dev_key`, `client.set_dev_key`, `DevKey`, `DevKeyList`, `Project.devKeys`
* Breaking: Removed `project.get_usage`, `UsageProject`, `MetricBreakdown` and `ProjectUsageRange`
* Breaking: Removed `organizations.cancel_downgrade`
* Breaking: `tables_db.cutover_migration` renamed to `tables_db.create_cutover`
* Breaking: `update_credentials` on `mysql`, `postgresql` and `mongo` returns a `DedicatedDatabaseOperation`
* Breaking: `domains.get_zone` returns the zone file as `str`
* Breaking: Removed `DedicatedDatabaseSpecificationList.pricing` and `DedicatedDatabaseSpecificationPricing`; rates moved onto each specification
* Breaking: Removed `projectName`, `region`, `organizationName`, `organizationId`, `billingPlan` and `reason` from `Block`
* Breaking: `BillingPlanGroup.STARTER` replaced by `FREE` and `START`
* Breaking: `OrganizationKeyScopes` devKeys and `organization.keys` scopes replaced by `ORGANIZATION_PROJECTS_KEYS_READ/WRITE`
* Breaking: Removed `EmbeddingModel.EMBEDDING_GEMMA` and `EmbeddingModel.BGE_SMALL`
* Breaking: Removed `DEV_KEYS`, `EXECUTIONS` and `STATS` from `QuerySuggestionResource`
* Breaking: `UsageEventMetric` dedicated database metrics dropped the `{databaseInternalId}` segment
* Breaking: `messaging.update_email`, `update_push` and `update_sms` reordered optional parameters; pass them by keyword
* Breaking: New optional parameters shift positions in `update_o_auth2_*`, `create_email`, `create_document(s)`; pass them by keyword
* Added: `growth` service with `create_conversation` and `create_installation`, plus `GrowthConversation` and `ConversationType`
* Added: `Topic` helper in `appwrite_console.topic` for building MQTT push topics
* Added: `account.create_id_token_session` for Apple and Google ID tokens, with `IdTokenProvider`
* Added: OTP email verification and recovery methods on `account`
* Added: `duration` on `create_email_password_session` and `current` on `delete_sessions`
* Added: organization project key methods, such as `organization.create_project_key` and `create_ephemeral_project_key`
* Added: Cloudflare, Kakao, Resend, TikTok and Webflow OAuth2 providers, with models and `update_o_auth2_*` methods
* Added: `prompt` on Auth0, Discord, GitHub, Kakao, Microsoft, Okta, Salesforce and Zoho OAuth2, with prompt enums
* Added: `native_client_ids` and `native_enabled` on Apple and Google OAuth2
* Added: `password-pwned` policy, `update_password_pwned_policy`, `PolicyPasswordPwned` and `User.passwordPwned`
* Added: Appwrite messaging provider, `create_appwrite_provider` and `update_appwrite_provider`
* Added: `qos` and `expiry` on topics, `reply_to_email`/`reply_to_name` on emails, `channel_id` on push
* Added: `domains.list_prices`, `DomainPricesList`, and `renewalPrice`/`renewalPeriodYears` on `DomainPrice`
* Added: `transaction_id` on `create_document` and `create_documents` in `documents_db` and `vectors_db`
* Added: storage resize fields and `credentialGeneration` on `DedicatedDatabase`; per-spec rates on `DedicatedDatabaseSpecification`
* Added: `dart-3.13` and `flutter-3.47` runtimes, `jaspr` framework and `ImageGravity.AUTO`
* Added: DocumentsDB, VectorsDB, `avatars.write` and `dedicatedDatabases.execute` project key scopes
* Added: request and network usage dimensions, plus matching optional fields on `UsageDataPoint`
* Added: `Project.firstAccessedAt`, `Project.mcpAccessedAt`, `Identity.providerIdToken`, `Installation.organizationUrl`
* Added: `BillingPlan.usageAggregateOnlyMetrics`, `BillingPlan.eligibleCountries`, function and site storage on `AggregationTeam`
* Added: `otpVerification` and `otpRecovery` email templates
* Updated: `domains.get_price` is deprecated in favour of `domains.list_prices`
* Updated: `DomainPrice.price`, `FrameworkAdapter.fallbackFile`, `TemplateFramework.fallbackFile` and `TemplateSite.demoUrl` are optional
* Fixed: `get_attribute` and `get_column` parse bigint, varchar, text and spatial types
* Fixed: `update_relationship_column` calls the correct endpoint path
* Fixed: Multipart requests without a file are sent as `multipart/form-data`
* Fixed: Empty strings for required path parameters raise `AppwriteException`

## 0.6.0

* Breaking: `Execution.functionId` replaced by `resourceId` and `resourceType`
* Breaking: `UsageEventMetric` and `UsageGaugeMetric` are plain string constants, not `Enum` members
* Breaking: `list_events` and `list_gauges` take `metrics` as plain strings
* Breaking: `UsageOrganizationProject` usage fields are single totals, not `List[Metric]`
* Breaking: `conditions`, `resourceData`, `items`, `discounts`, `authorizationDetails` and `rows` are lists, not dicts
* Breaking: Removed `ProjectKeyScopes.DEDICATEDDATABASES_EXECUTE`
* Breaking: `Addon` enum renamed to `AddonKey`; `get_addon_price` takes `AddonKey`
* Added: `huggingface` OAuth2 provider, `OAuth2HuggingFace` and `update_o_auth2_hugging_face`
* Added: `avatars.get_photo` for Gravatar-backed profile photos
* Added: `scopes` on `sites.create`, `sites.update` and `Site`
* Added: `strategy` and `max_bucket_size` on WAF rate limit rules
* Added: `bun-1.4` runtime and build runtime
* Added: usage metrics for webhook events, phone auth, messages, per-service build mbSeconds and WAF challenges
* Added: `BillingPlan.databaseComputeCredit` and `BillingPlan.supportsDedicatedDatabases`
* Added: `Database.lifecycleState`, `Database.containerStatus` and `Database.error`
* Added: `DatabaseMigration.changelogWatermark`, `replicating` on replicas and members, `DedicatedDatabaseBranchList.total`
* Added: `_APP_VCS_PROVIDERS_WITH_PUBLIC_REPOSITORIES` and `_APP_VCS_PROVIDERS_WITH_REPOSITORY_CREATION`
* Fixed: chunked uploads only probe for prior progress when an `upload_id` is given
* Updated: `Project.wafEnabled` and `UsageDataPoint.time` are optional

## 0.5.0

* Breaking: `Preferences` serializes its keys at the top level, not nested under `data`
* Added: `target_database_id` on `create_restoration` for `mysql`, `postgresql`, and `mongo`
* Added: `DedicatedDatabaseRestoration.sourceDatabaseId`, the database a backup was restored from
* Fixed: `Document` and `Row` serialize nested `data` honouring `by_alias` and `exclude_*`
* Fixed: `AppwriteException` carries the raw `response` when parsing into a model fails
* Updated: `DedicatedDatabaseRestoration.databaseId` documents the database restored into
* Updated: relationship `type` and `on_delete` docstrings list their allowed values
* Updated: column type docstrings list `double` and the spatial types

## 0.4.0

* Breaking: Removed `standby_region` and `cross_region_replicas` from `mysql`, `postgresql`, and `mongo`
* Breaking: Removed `DedicatedDatabase.crossRegionReplicas` and `DedicatedDatabaseSpecificationPricing.crossRegionReplicaRate`
* Breaking: `PlanChangeLimits.projects` is now a `PlanChangeResourceCompliance`; per-project details moved to `projectCompliance`
* Breaking: Removed `PlanChangeLimits.totalProjects`, superseded by `projects.currentUsage`
* Added: `affiliates` service, with affiliate link, referral, and reward models
* Added: `proxy.create_invalidation` to purge CDN cache by tag, path, or domain
* Added: `tables_db.cutover_migration`, and `auto_cutover` on `create_migration`
* Added: `project.update_mfa_factors_policy` and the `mfa-factors` policy
* Added: `users.get_mfa_challenge`, returning the code for a custom MFA challenge
* Added: `custom` authentication factor on `AuthenticationFactor` and `MfaFactors`
* Added: `installation_scopes` on `project.update_o_auth_2_server`
* Added: `aggregate` on `usage.list_gauges`, for peak values over a window
* Added: `UsageEventMetric` and `UsageGaugeMetric` enums for `usage` metric names
* Added: `PlanChangeLimits.members` and `PlanChangeLimits.domains` compliance
* Updated: `usage.list_events` and `list_gauges` type `metrics` as enums
* Updated: `DatabaseMigration` reports `cutoverRequested`
* Updated: `syncStateConfirmed` is optional, and absent when no engine was probed

## 0.3.0

* Added: `UsageInterval`, `UsageEventDimension`, `UsageGaugeDimension`, `UsageOrderBy`, and `UsageOrderDirection` enums
* Updated: `list_events` and `list_gauges` accept those enums for `interval`, `dimensions`, `order_by`, and `order_dir`
* Fixed: `UsageProject` text embedding fields are lists of `Metric`, and their totals are numbers
* Fixed: `get_session`, `update_session`, and `delete_session` require `session_id` again

## 0.2.1

* Fixed: `Organization` accepts null for the billing, agreement, and startup program fields the server leaves unset
* Fixed: `BillingPlan` accepts plans that omit `usage.member`, `usage.realtimeBandwidth`, or `usage.credits`
* Fixed: `BillingPlan` accepts plans that omit the `seats` and `projects` addons, or an addon's `currency`

## 0.2.0

* Fixed: `list_regions` accepts a null `available`, which the server returns when access is unresolved
* Fixed: `Domain.transferStatus` accepts no status for a domain that is not being transferred
* Fixed: `Organization.billingBudget` accepts null when no budget is set
* Fixed: `BillingPlan` accepts plans that omit `members`, `activityLogs`, `backupsEnabled`, or `backupPolicies`
* Removed: `assistant` and `manager` services, which are internal to Cloud

## 0.1.0

* Added: First release of the Console Python SDK
