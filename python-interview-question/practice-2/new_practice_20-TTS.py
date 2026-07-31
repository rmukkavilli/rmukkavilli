import time
class TTLCache:
    def __init__(self):
        self.cache:dict = {}

    def put(self, key: str, value: object, ttl_seconds: float) -> None:
        expiration_time = time.monotonic() + ttl_seconds
        self.cache[key] = (value, expiration_time)
        

    def get(self, key: str) -> object | None:
        if key not in self.cache:
            return None

        value, expiration_time = self.cache[key]

        if time.monotonic() >= expiration_time:
            del self.cache[key]
            return None

        return value



cache = TTLCache()

cache.put("token", "abc123", 2)

print(cache.get("token"))  # "abc123"

time.sleep(2)

print(cache.get("token"))  # None