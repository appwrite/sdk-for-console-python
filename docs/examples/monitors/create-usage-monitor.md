```python
from appwrite_console.client import Client
from appwrite_console.services.monitors import Monitors
from appwrite_console.models import Monitor
from appwrite_console.enums.monitor_severity import MonitorSeverity
from appwrite_console.query import Query

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

monitors = Monitors(client)

result: Monitor = monitors.create_usage_monitor(
    monitor_id = '<MONITOR_ID>',
    name = '<NAME>',
    rules = [
        Query.greater_than('network.outbound', 5000000000)
    ],
    window = 3600, # optional
    cooldown = 1800, # optional
    enabled = True, # optional
    notify = ["owner"], # optional
    severity = MonitorSeverity.INFO, # optional
    escalation_id = '<ESCALATION_ID>' # optional
)

print(result.model_dump())
```
