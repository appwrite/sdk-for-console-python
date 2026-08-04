# Change Log

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
