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
        result = len(cache.dict)
        self.assertEqual(result, 1, 'Put test Passed')
    
    def test_delete(self):
        cache = LRUCache(2)
        cache.put(1,'One')
        cache.put(2,'Two')
        cache._del(1)
        result = len(cache.dict)
        self.assertEqual(result, 1, 'Delete test Passed')
        
    def test_reset(self):
        cache = LRUCache(2)
        cache.put(1,'One')
        cache.put(2,'Two')
        cache.reset()
        result = len(cache.dict)
        self.assertEqual(result, 0, 'Reset test Passed')
    
    def test_capacity_exceed(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(2,4)
        cache.put(3, 3)
        result = 1 not in cache.list
        result2 = len(cache.dict)
        self.assertEqual(result, True, 'Reset test Passed')
        self.assertEqual(result2, 2, 'Reset test Passed')
        
if __name__ == '__main__':
    unittest.main()