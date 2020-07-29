# LRU cache - least recently used
# Create LRU cache with max cache size (3 values)
# If try to insert 4th value, remove least recent and insert 4th value
#
# cache = new LruCache(3)
#
# cache.put(1, "a") // add "a" cache
# cache.put(2, "b" // add "b" cache
# cache.put(3, "c") // add "c" cache
# cache.put(4, "d") // remove "a" from cache and add "d"


# cache = new LruCache(3)
#
# cache.put(1, "a") // add "a" cache
# cache.put(2, "b" // add "b" cache
# cache.put(3, "c") // add "c" cache
# cache.get(1) // return "a"
# cache.put(4, "d") // remove "b" and add "d"
from collections import OrderedDict 


class LruCache:
    def __init__(self, size):
        self.cache = OrderedDict()
        # {1: "a", 2: b, 3:"c"}
        self.size = size
        
    def put(self, index, char):
        if len(self.cache) < self.size:
            self.cache[index] = char
        else:
            self.cache.popitem(last=False)  
            self.cache[index] = char

    def get(self, index):
        # TODO: If key doesn't exist, add error
        value = self.cache.pop(index)
        self.cache[index] =value
        return value

cache = LruCache(3)
cache.put(1, "a") 
cache.put(2, "b") 
cache.put(3, "c")
assert cache.get(1) == "a"
cache.put(4, "d") 
# for key, value in cache.cache.items():
#     print(key, value)
# should return error because there is nothing with value of 2
assert cache.get(4) == "d"
