# Least-Recently Used (LRU) Cache Implementation
Least-Recently Used (LRU) Cache Implementation in Python with the help of Dictionary and List data structure.

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Files and Description](#Files-and-Description)
* [Setup](#setup)
* [Code Examples](#Code-Examples)
* [Status](#status)
* [Contact](#contact)

## General info
This is LRU Cache implementation which will have its maximum capacity set at the time of the construction, and when adding new keys that cause the capacity to be exceeded, the “least recently used” item needs to be identified and discarded. This LRU is implemented with five different methods described in Files and Description section.

## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
Project is created with:
* Python - version 3.7.5

## Files and Description
 Markup : 1. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered
          
          
This reposetory contains following three files

1. **LRU.py** - This file contains the implementation of the LRU with the list and dictionary data staructure. This implementation posseses following five methods.
 * get(key) - Returns the value of a key, if it exists.
 * put(key, val) - Creates new key and adds it to the cache and updates key value pair if key already exists
 * _del(key) - Remove the key and its value from the cache memory. If key does not exist no operation will be performed
 * reset() - clear the cache memory
 * _print() - This method is used to print the cache memory in the order from least to recent.

## Setup
Describe how to install / setup your local environement / add link to demo version.

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
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!



 
