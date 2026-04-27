import time
from typing import Any, Optional, Dict

class InMemoryCache:
    def __init__(self):
        # Store is a dict: {key: (value, expiration_time)}
        self._store: Dict[str, tuple] = {}

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        
        value, expiration = self._store[key]
        if time.time() > expiration:
            del self._store[key]
            return None
        
        return value

    def set(self, key: str, value: Any, ttl_seconds: int = 600):
        expiration = time.time() + ttl_seconds
        self._store[key] = (value, expiration)

    def delete(self, key: str):
        if key in self._store:
            del self._store[key]

    def clear(self):
        self._store = {}

# Global cache instance
query_cache = InMemoryCache()
