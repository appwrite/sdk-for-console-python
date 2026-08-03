```python
from appwrite_console.client import Client
from appwrite_console.services.manager import Manager
from appwrite_console.models import BlockList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint

manager = Manager(client)

result: BlockList = manager.list_blocks(
    project_id = '<PROJECT_ID>'
)

print(result.model_dump())
```
