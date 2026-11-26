```python
from appwrite_console.client import Client
from appwrite_console.services.alerts import Alerts
from appwrite_console.models import Alert

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

alerts = Alerts(client)

result: Alert = alerts.get(
    alert_id = '<ALERT_ID>'
)

print(result.model_dump())
```
