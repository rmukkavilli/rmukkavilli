class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = capacity
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive integer capacity.
        """
        self.capacity = capacity
        self.cache : dict[int, Node] ={}
        self.left.next  = self.right 
        self.next.prev = self.left
        


    def get(self, key: int) -> int:
        """
        Return the value of the key if it exists, otherwise return -1.
        If the key is accessed, it becomes most recently used.
        """
        if key not in self.cache:
            return -1
        
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._insert_mru(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert_mru(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next

            self._remove(lru)
            del self.cache[lru.key]
        
        return node.value


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))  # 1

cache.put(3, 3)      # Evicts key 2
print(cache.get(2))  # -1

cache.put(4, 4)      # Evicts key 1
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4