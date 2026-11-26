```python
from appwrite_console.client import Client
from appwrite_console.services.videos import Videos
from appwrite_console.models import VideoCodecList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

videos = Videos(client)

result: VideoCodecList = videos.list_codecs()

print(result.model_dump())
```
