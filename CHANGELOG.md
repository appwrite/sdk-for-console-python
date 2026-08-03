# Change Log

## 0.2.0

* Fixed: `list_regions` accepts a null `available`, which the server returns when access is unresolved
* Fixed: `Domain.transferStatus` accepts no status for a domain that is not being transferred
* Fixed: `Organization.billingBudget` accepts null when no budget is set
* Fixed: `BillingPlan` accepts plans that omit `members`, `activityLogs`, `backupsEnabled`, or `backupPolicies`
* Removed: `assistant` and `manager` services, which are internal to Cloud

## 0.1.0

* Added: First release of the Console Python SDK
