# Least-Recently Used (LRU) Cache Implementation
Least-Recently Used (LRU) Cache Implementation in Python with the help of Dictionary and List data structure.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Files and Description](#Files-and-Description)
* [Setup](#setup)
* [Code Examples](#Code-Examples)
* [Status](#status)
* [Contact](#contact)

## General info
This is LRU Cache implementation which will have its maximum capacity set at the time of the construction, and when adding new keys that cause the capacity to be exceeded, the “least recently used” item needs to be identified and discarded. This LRU is implemented with five different methods described in Files and Description section.

## Technologies
Project is created with:
* Python - version 3.7.5

## Files and Description

This reposetory contains following three files

1. **LRU.py** - This file contains the implementation of the LRU with the list and dictionary data staructure. This implementation posseses following five methods.
 * get(key) - Returns the value of a key, if it exists.
 * put(key, val) - Creates new key and adds it to the cache and updates key value pair if key already exists
 * _del(key) - Remove the key and its value from the cache memory. If key does not exist no operation will be performed
 * reset() - clear the cache memory
 * _print() - This method is used to print the cache memory in the order from least to recent.

2. **LRU_test.py** - This .py file contains different unit test for the implementation. Following test cases are considered.
 * Capacity test - Cache must be initialized with a maximum size
 * Get test - get the value of a key
 * Put test - Put the value of a new key
 * Update test - Update the value for existing key
 * Delete test - delete a key. Attempting to delete a key that doesn’t exist is a no-op
 * Reset test - reset the cache, which will remove all items from the cache 
 * Least Recently used memory removal test - Based on the hotness of the key least recently used memory removed when maximum capacity exceeded
 * Maximum capacity not exceeded test - Checking maximum capacity exceeded or not

3. **main.py** - This file contains example demonstration of the LRU cache with different methods.
 
## Setup
The Unit tests can be run by the following commands on windows command prompt,
```
git clone https://github.com/rr8shah/LRU.git
cd LRU
python LRU_test.py

```
The example file can be run by the following commands on windows command prompt,
```
git clone https://github.com/rr8shah/LRU.git
cd LRU
python main.py

```

## Code Examples
Example usage of the LRU implementation:
```
from LRU import LRUCache

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache._print()
cache.get(2)
cache.put(4, 4)
cache._print()
cache.get(3)
cache.get(4)
cache.get(2)
cache._del(4)
cache._print()
cache.get(4)
cache.reset()
cache._print()
cache.get(1)
```

## Status
Project is: _finished_

## Contact
Created by [@rr8shah](https://github.com/rr8shah) - feel free to contact me!!
 
