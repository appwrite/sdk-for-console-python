```python
from appwrite_console.client import Client
from appwrite_console.services.monitors import Monitors

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

monitors = Monitors(client)

result = monitors.delete(
    monitor_id = '<MONITOR_ID>'
)
```
