class LRUCache:
    '''
    LRU Cache implementation using a Dictionary and a list.
    
    Dictionary acts as a cache memory while list keeps track of the 
    order in which key is accessed.
    
    ...............
    
    Attributes
    ----------
    capacity : int
        The maximum capacity of the cache memory while initialized
    keys : list
        list which keeps track of the order in which key is accessed.
    cache : dictionary
        this dictionary acts as a cache memory and holds key-value pair
        
        
    Methods
    -------
    get(key) - Returns the value of a key, if it exists.
    put(key, val) - Creates new key and adds it to the cache.
                  - updates key value if key already exists
    _del(key) - Remove the key and its value from the cache memory
    reset() - clear the cache memory
    _print() - This method is used to print the cache memory in the order from least to recent.
    
    '''
    # constructor of the class
    def __init__(self, capacity: int):
        self.cache = dict() # This dictionary acts as the cache memory
        self.keys = list() # This list keeps track of the order of the keys recently used
        self.capacity = capacity # Initialized capacity
    
    
    def get(self, key):
        '''This get function returns the value for the requested key 
        and rearrange its order in the list based on its recent use'''
        
        if key in self.keys:
            if self.keys[-1] != key:
                self.keys.remove(key)                      
                self.keys.append(key)                      
                print("The value returned is ", self.cache[key])
                return self.cache[key]
            else:
                print("The value returned is ", self.cache[key])
                return self.cache[key]
        else: 
            print("Key can not be found in the cache")
    

    def put(self, key , value) -> None:
        '''This put function create or update the key value 
        pair in cache keeping track of the key order in list.
        When adding new keys that cause the capacity to be 
        exceeded, the “least recently used” key is identified 
        and discarded by this function'''
        
        # if key is present then update the value and check the length.
        if key in self.keys:               
            if len(self.keys) <= self.capacity:
                self.cache[key] = value
                self.keys.remove(key)
                self.keys.append(key)
                print("Value updated in the existing key")
        
        # if key is not present then create the key and value pair in cache memory
        else:
            self.keys.append(key)         
            self.cache[key] = value
            #if length exceeds then remove the least used memory
            if len(self.keys) > self.capacity:       
                key_to_be_removed = self.keys[0]
                self.cache.pop(key_to_be_removed)
                self.keys.pop(0)
                print("New key and value pair created in the cache with the removal of the least recently used key and value")
            else:
                print("New key and Value pair created in the cache")
                
    
    def _del(self, key):
        '''This function remove the valid key and value pair from cache. 
        If key is not present than no operation is performed'''
        
        if key in self.keys:
            self.keys.remove(key)
            self.cache.pop(key)
            print("Given key and corresponsing value are successfully removed from the cache")
        else:
            print('Key can not be found in the cache and No deletion operation is performed')
            
    
    def reset(self):
        '''This function reset the cache to its maximum capacity'''
        
        self.keys.clear()
        self.cache.clear()
        print("Cache is cleared")
    
    
    def _print(self):
        '''This function is used to print the cache memory in order'''
        
        print('-----------------------------------------')
        print("Ordered cache from least to recent use")
        for key in self.keys:
            print('{}: {}'.format(key, self.cache[key]))
        print('-----------------------------------------')