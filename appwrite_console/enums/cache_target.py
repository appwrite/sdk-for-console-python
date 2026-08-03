from enum import Enum

class CacheTarget(Enum):
    CACHE = "cache"
    TIMELIMIT = "timelimit"
    LOCKS = "locks"
    PUBSUB = "pubsub"
    QUEUE = "queue"
    ALL = "all"
