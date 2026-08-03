```python
from appwrite_console.client import Client
from appwrite_console.services.manager import Manager
from appwrite_console.enums import Region
from appwrite_console.enums import CacheTarget
from appwrite_console.enums import CacheDatabase

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint

manager = Manager(client)

result = manager.delete_cache(
    region = Region.FRA, # optional
    cache = CacheTarget.CACHE, # optional
    all = False, # optional
    database = CacheDatabase.CONSOLE, # optional
    project_id = '<PROJECT_ID>', # optional
    collection_id = '<COLLECTION_ID>', # optional
    document_id = '<DOCUMENT_ID>' # optional
)
```
