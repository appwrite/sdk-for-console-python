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

result: Monitor = monitors.update_tcp_monitor(
    monitor_id = '<MONITOR_ID>',
    name = '<NAME>', # optional
    host = 'db.example.com', # optional
    port = 5432, # optional
    rules = [
        Query.greater_than('latency', 1000)
    ], # optional
    interval = 60, # optional
    timeout = 10, # optional
    cooldown = 300, # optional
    enabled = True, # optional
    notify = ["owner"], # optional
    severity = MonitorSeverity.INFO, # optional
    escalation_id = '<ESCALATION_ID>' # optional
)

print(result.model_dump())
```
