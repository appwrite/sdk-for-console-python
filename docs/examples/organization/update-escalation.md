```python
from appwrite_console.client import Client
from appwrite_console.services.organization import Organization
from appwrite_console.models import Escalation

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

organization = Organization(client)

result: Escalation = organization.update_escalation(
    escalation_id = '<ESCALATION_ID>',
    name = '<NAME>', # optional
    steps = [
	    {
	        "delay": 0,
	        "roles": [
	            "owner"
	        ]
	    },
	    {
	        "delay": 900,
	        "roles": [
	            "developer"
	        ],
	        "userIds": [
	            "<USER_ID>"
	        ]
	    }
	], # optional
    repeat = 1 # optional
)

print(result.model_dump())
```
