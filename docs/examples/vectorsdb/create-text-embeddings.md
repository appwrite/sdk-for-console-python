```python
from appwrite_console.client import Client
from appwrite_console.services.vectors_db import VectorsDB
from appwrite_console.models import EmbeddingList
from appwrite_console.enums import EmbeddingModel

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

vectors_db = VectorsDB(client)

result: EmbeddingList = vectors_db.create_text_embeddings(
    texts = [],
    model = EmbeddingModel.NOMIC_EMBED_TEXT # optional
)

print(result.model_dump())
```
