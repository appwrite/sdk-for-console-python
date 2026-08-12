# Change Log

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
