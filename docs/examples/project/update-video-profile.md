```python
from appwrite_console.client import Client
from appwrite_console.services.project import Project
from appwrite_console.models import VideoProfile

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

project = Project(client)

result: VideoProfile = project.update_video_profile(
    profile_id = '<PROFILE_ID>',
    name = '<NAME>', # optional
    video_bit_rate = 32000, # optional
    audio_bit_rate = 32000, # optional
    width = 16, # optional
    height = 16 # optional
)

print(result.model_dump())
```
