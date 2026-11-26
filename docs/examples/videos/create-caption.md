```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import VideoCaption

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: VideoCaption = videos.create_caption(
    video_id = '<VIDEO_ID>',
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>',
    name = '<NAME>',
    language = 'aar',
    default = False # optional
)

print(result.model_dump())
```
