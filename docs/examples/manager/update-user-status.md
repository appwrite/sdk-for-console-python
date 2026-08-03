```python
from appwrite_console.client import Client
from appwrite_console.services.manager import Manager
from appwrite_console.models import User

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint

manager = Manager(client)

result: User = manager.update_user_status(
    status = False,
    user_id = '<USER_ID>', # optional
    email = '<EMAIL>', # optional
    reason = '<REASON>' # optional
)

print(result.model_dump())
```
