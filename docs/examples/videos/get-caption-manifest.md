```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.enums.video_output import VideoOutput

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: bytes = videos.get_caption_manifest(
    video_id = '<VIDEO_ID>',
    output = VideoOutput.HLS,
    caption_id = '<CAPTION_ID>'
)
```
