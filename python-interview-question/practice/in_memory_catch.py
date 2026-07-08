import time
class TTLCache:
    
    def __init__(self):
        self.data = {} 
    
    def put(self, key: str, value: str, ttl: float):
        """Store a value with expiration time (ttl in seconds)."""
        expiration_time = time.time() + ttl
        self.data[key] = {"value": value, "expires_at": expiration_time}

    def get(self, key: str) -> str | None:
        """
        Return the value if it exists and is not expired.
        Return None if the key doesn't exist or is expired.
        """
        if key not in self.data:
            return None
        entry = self.data[key]
        if time.time() > entry["expires_at"]:
            del self.data[key]
            return None
        return entry["value"]

def test_ttl_cache_postitive():
    print("testign test_ttl_cache_postitive")
    ttl = TTLCache()
    ttl.put("test", "13", 1.0)
    assert ttl.get("test") == "13"

def test_ttl_cache_None():
    ttl = TTLCache()
    ttl.put("test", "13", -1.0)
    assert ttl.get("test") is None