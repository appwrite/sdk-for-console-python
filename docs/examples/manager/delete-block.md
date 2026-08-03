```python
from appwrite_console.client import Client
from appwrite_console.services.manager import Manager
from appwrite_console.models import BlockDelete
from appwrite_console.enums import BlockResourceType

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint

manager = Manager(client)

result: BlockDelete = manager.delete_block(
    project_id = '<PROJECT_ID>',
    resource_type = BlockResourceType.PROJECTS,
    resource_id = '<RESOURCE_ID>' # optional
)

print(result.model_dump())
```
