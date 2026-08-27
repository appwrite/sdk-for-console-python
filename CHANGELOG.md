# Change Log

## 0.6.0

* Breaking: `Execution.functionId` replaced by `resourceId` and `resourceType`
* Breaking: `UsageEventMetric` and `UsageGaugeMetric` are plain string constants, not `Enum` members
* Breaking: `list_events` and `list_gauges` take `metrics` as plain strings
* Breaking: `UsageOrganizationProject` usage fields are single totals, not `List[Metric]`
* Breaking: `conditions`, `resourceData`, `items`, `discounts`, `authorizationDetails` and `rows` are lists, not dicts
* Breaking: `get_addon_price` takes `Addon`, renamed from `AddonEnum`
* Breaking: Removed `ProjectKeyScopes.DEDICATEDDATABASES_EXECUTE`
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
* Fixed: `Addon` response model no longer shadowed by the `Addon` enum in `organizations`
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
