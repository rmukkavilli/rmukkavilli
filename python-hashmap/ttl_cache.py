import time
class TTLCache:

    def __init__(self):
        self.cache = {}

    def put(self, key, value, ttl):
        ...
        expiration_time = time.time() + ttl
        self.cache[key] = (value, expiration_time)

    def get(self, key):
        if key not in self.cache:
            return None
        
        value, expiration_time = self.cache[key]
        
        if time.time() >= expiration_time:
            del self.cache[key]
            return None
        return value


cache = TTLCache()
cache.put("123", "test", 3)
time.sleep(4)
print(cache.get("123"))
cache.put("123", "aaaa", 20)
time.sleep(10)
cache.put("456", "aaaa", 20)
print(cache.get("123"))
print(cache.get("456"))
