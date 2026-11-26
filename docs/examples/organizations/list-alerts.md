```python
from appwrite_console.client import Client
from appwrite_console.services.organizations import Organizations
from appwrite_console.models import AlertList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

organizations = Organizations(client)

result: AlertList = organizations.list_alerts(
    organization_id = '<ORGANIZATION_ID>',
    queries = [], # optional
    total = False # optional
)

print(result.model_dump())
```
