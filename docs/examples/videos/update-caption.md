```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import VideoCaption

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: VideoCaption = videos.update_caption(
    video_id = '<VIDEO_ID>',
    caption_id = '<CAPTION_ID>',
    bucket_id = '<BUCKET_ID>', # optional
    file_id = '<FILE_ID>', # optional
    name = '<NAME>', # optional
    language = 'aar', # optional
    default = False # optional
)

print(result.model_dump())
```
