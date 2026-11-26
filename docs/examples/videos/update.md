```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import Video
from appwrite_console.permission import Permission
from appwrite_console.role import Role

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: Video = videos.update(
    video_id = '<VIDEO_ID>',
    name = '<NAME>', # optional
    permissions = [Permission.read(Role.any())] # optional
)

print(result.model_dump())
```
