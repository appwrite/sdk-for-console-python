```python
from appwrite_console.client import Client
from appwrite_console.services.monitors import Monitors
from appwrite_console.models import Monitor

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

monitors = Monitors(client)

result: Monitor = monitors.get(
    monitor_id = '<MONITOR_ID>'
)

print(result.model_dump())
```
