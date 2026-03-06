# Build a simple cache
# -> implement a small cache
# -> When capacity is exceeded, remove the oldest item.

# cache = Cache(capacity=2)
#
# cache.put("a", 1)
# cache.put("b", 2)
# cache.get("a") -> 1
# cache.put("c", 3)
# cache.get("b") -> None

class Cache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.values = {}

    def get(self, index: str) -> int|None:
        if index not in self.values:
            return None

        value = self.values.pop(index)
        self.values[index] = value  # move to most recent
        return value

    def put(self, index: str, value: int) -> None:
        if index in self.values:
            self.values.pop(index)
        elif len(self.values) >= self.cap:
            oldest = next(iter(self.values)) # find the oldest, that is the first element in the dictionary
            self.values.pop(oldest)

        self.values[index] = value


cache = Cache(capacity=2)

cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a")) # -> 1
cache.put("c", 3)
print(cache.get("b")) # -> None