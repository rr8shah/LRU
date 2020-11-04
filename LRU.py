class LRUCache:
    # initialising capacity
    def __init__(self, capacity: int):
        self.dict = dict() # This dictionary acts as the cache memory
        self.list = list() # This list keeps track of the order of the keys recently used
        self.capacity = capacity # Initialized capacity
    
    '''This get function gives the value for the requested key and rearrange its order in the list based on its recent use'''
    def get(self, key):
        if key in self.list:
            if self.list[-1] != key:
                self.list.remove(key)                      
                self.list.append(key)                      
                print("The value returned is ", self.dict[key])
                return self.dict[key]
            else:
                print("The value returned is ", self.dict[key])
                return self.dict[key]
        else: 
            print("Key can not be found in the cache")
    
    '''This put function create or update the key value pair in cache keeping track of the key order in list'''
    '''When adding new keys that cause the capacity to be exceeded, the “least recently used”
       key is identified and discarded by this function'''
    def put(self, key , value) -> None:
        if key in self.list:               # if key is present then update the value and check the length.
            if len(self.list) <= self.capacity:
                self.dict[key] = value
                self.list.remove(key)
                self.list.append(key)
                print("Value updated in the existing key")
        else:
            self.list.append(key)         # if key is not present then create the key and value pair in cache memory
            self.dict[key] = value
            if len(self.list) > self.capacity:      #if length exceeds then remove the least used memory 
                key_to_be_removed = self.list[0]
                self.dict.pop(key_to_be_removed)
                self.list.pop(0)
                print("New key and value pair created in the cache with the removal of the least recently used key and value")
            else:
                print("New key and Value pair created in the cache")
                
    '''This function remove the valid key and value pair from cache. If key is not present than no operation is performed'''
    def _del(self, key):
        if key in self.list:
            self.list.remove(key)
            self.dict.pop(key)
            print("Given key and corresponsing value are successfully removed from the cache")
        else:
            print('Key can not be found in the cache and No deletion operation is performed')
            
    '''This function reset the cache to its maximum capacity'''
    def reset(self):
        self.list.clear()
        self.dict.clear()
        print("Cache is cleared")
    
    '''This function is used to print the cache memory in order'''
    def _print(self):
        print("Ordered cache from least to recent use")
        for key in self.list:
            print('{}: {}'.format(key, self.dict[key]))
        print('-----------------------------------------')