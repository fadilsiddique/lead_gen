import time

class Cache:
    def __init__(self):
        self.store = {}

    def get(self, key):
        data = self.store.get(key)
        if not data:
            return None

        value, expiry = data
        if expiry < time.time():
            del self.store[key]
            return None

        return value

    def set(self, key, value, ttl=3600):
        expiry = time.time() + ttl
        self.store[key] = (value, expiry)
