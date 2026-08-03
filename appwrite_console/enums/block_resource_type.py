from enum import Enum

class BlockResourceType(Enum):
    PROJECTS = "projects"
    FUNCTIONS = "functions"
    SITES = "sites"
    DATABASES = "databases"
    BUCKETS = "buckets"
    PROVIDERS = "providers"
    TOPICS = "topics"
    SUBSCRIBERS = "subscribers"
    MESSAGES = "messages"
