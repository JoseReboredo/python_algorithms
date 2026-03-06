# LRU Cache

# Problem
# -> Implement a cache with capacity
# put(key, value)
# get(key)
# Constraint
# -> get and put must be O(1)

# Rules
# - max size = capacity
# - when capacity exceeded → remove least recently used

# Example
# capacity = 2
#
# put("a",1)
# put("b",2)
# get("a") -> 1
# put("c",3)
#
# get("b") -> None
# -> Meaning b was evicted.

from collections import deque
# tried with queues but I have a problem how to remove an element in an index position to add it again later

class LruCacheDeQue:
    def __init__(self, cap: int):
        self.cache = deque()
        self.capacity = cap

    def put(self, key: str, value: int) -> None:
        if len(self.cache) == self.capacity:
            self.cache.popleft()
        self.cache.append((key, value))


    def get(self, key) -> int|None:
        try:
            index = self.cache.index(key)
        except ValueError:
            return None

        element = self.cache[index]

        self.cache.remove(element)
        self.cache.append(element)

        return element[1]

# let's try with a dictionary

class LruCache:
    def __init__(self, cap: int):
        self.cache = {}
        self.capacity = cap

    def put(self, key: str, value: int) -> None:
        # if we are planning to refresh the already existing key we remove this one
        # not sure if to move it inside hte next if to make it more efficient
        if key in self.cache:
            self.cache.pop(key)

        if len(self.cache) == self.capacity:
            k = next(iter(self.cache))
            self.cache.pop(k)

        self.cache[key] = value


    def get(self, key) -> int|None:
        value = self.cache.get(key)
        if value is not None:
            self.cache.pop(key)
            self.cache[key] = value

        return value

# Hashmap/dictionaries + Double linked list
# key -> node (O(1) lookup)
# node <-> node <-> node  (usage order)
# De ChatGPT.. no me convence mucho.

class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LruCacheWithNodes:
    def __init__(self, cap: int):
        self.cache = {}
        self.capacity = cap

        self.left = Node(0, 0)  # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

capacity = 2

cache = LruCache(capacity)
cache.put("a",1)
cache.put("b",2)
print(cache.get("a")) # 1

cache.put("c",3)
print(cache.get("b")) # None

