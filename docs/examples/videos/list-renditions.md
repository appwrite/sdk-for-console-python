```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import VideoRenditionList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: VideoRenditionList = videos.list_renditions(
    video_id = '<VIDEO_ID>',
    queries = [], # optional
    total = False # optional
)

print(result.model_dump())
```
