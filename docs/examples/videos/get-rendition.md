```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import VideoRendition

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: VideoRendition = videos.get_rendition(
    video_id = '<VIDEO_ID>',
    rendition_id = '<RENDITION_ID>'
)

print(result.model_dump())
```
