from LRU import LRUCache
import unittest

class TestLRU(unittest.TestCase):
    
    # Standard test case of the key requirements listed in the Coding Assignment PDF
    def test_capacity(self):
        cache = LRUCache(2)
        result = cache.capacity
        self.assertEqual(result, 2, 'Capacity test Passed')
    
    def test_get(self):
        cache = LRUCache(2)
        cache.put(1,'One')
        result = cache.get(1)
        self.assertEqual(result, 'One', 'Get test Passed')
    
    def test_put(self):
        cache = LRUCache(2)
        cache.put(1,'One')
        result = len(cache.cache)
        self.assertEqual(result, 1, 'Put test Passed')
    
    def test_delete(self):
        cache = LRUCache(2)
        cache.put(1,'One')
        cache.put(2,'Two')
        cache._del(1)
        result = len(cache.cache)
        self.assertEqual(result, cache.capacity - 1, 'Delete test Passed')
        
    def test_reset(self):
        cache = LRUCache(2)
        cache.put(1,'One')
        cache.put(2,'Two')
        cache.reset()
        result = len(cache.cache)
        self.assertEqual(result, 0, 'Reset test Passed')
    
    #Checking edge cases of the memory exceed
    def test_capacity_exceed(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(2,4)
        cache.put(3, 3)
        result = 1 not in cache.keys
        result2 = len(cache.cache)
        self.assertEqual(result, True, 'Least Recently used memory removal test Passed')
        self.assertEqual(result2, cache.capacity, 'Maximum capacity not exceeded test Passed')
        
if __name__ == '__main__':
    unittest.main()