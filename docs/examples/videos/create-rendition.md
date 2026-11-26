```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import VideoRendition
from appwrite_console.enums.video_output import VideoOutput

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: VideoRendition = videos.create_rendition(
    video_id = '<VIDEO_ID>',
    profile_id = '<PROFILE_ID>',
    output = VideoOutput.HLS
)

print(result.model_dump())
```
