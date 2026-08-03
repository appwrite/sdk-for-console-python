```python
from appwrite_console.client import Client
from appwrite_console.services.manager import Manager
from appwrite_console.models import Block
from appwrite_console.enums import BlockResourceType
from appwrite_console.enums import BlockMode

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint

manager = Manager(client)

result: Block = manager.create_block(
    project_id = '<PROJECT_ID>',
    resource_type = BlockResourceType.PROJECTS,
    resource_id = '<RESOURCE_ID>', # optional
    mode = BlockMode.FULL, # optional
    reason = '<REASON>', # optional
    expired_at = '2020-10-15T06:38:00.000+00:00' # optional
)

print(result.model_dump())
```
