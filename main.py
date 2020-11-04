from LRU import LRUCache
import time


cache = LRUCache(2)
start = time.time()
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
cache.get(2)
end = time.time()
print('Time taken to execute', end - start, 'seconds')
