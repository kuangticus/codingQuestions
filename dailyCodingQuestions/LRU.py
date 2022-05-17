#LRU Implementation with orderedDict 
#from scratch

from collections import OrderedDict


class LRU(OrderedDict):

    def __init__(self, capacity: int):

        #define the capacity upon creation instantion
        # constructor
        self.capacity = capacity
    
    def put(self, key: int, value: int):
        
        if key in self:
            # since this is most recent added then move it to end of the of the order Dict
            self.move_to_end(key)
        
        self[key] = value

        if len(self) > self.capacity:
            # we pop the least used which is the most topest item:
            # last equals false, since we don't want to move the most recently used

            self.popitem(last=False)

    def get(self, key: int) -> int:
        
        # as stated by prompt if not in the cache return -1 
        if key not in self:
            return -1
        else:
            return self[key]

 
 
# Testing Cases 
# lru = LRU(10)

# lru.put(10, 1)
# lru.put(12, 2)
# lru.put(15, 2)
# lru.put(16, 2)
# lru.put(17, 2)


# print(lru.get(10))
# print(lru.get(12))
# print(lru.get(15))
# print(lru.get(16))
# print(lru.get(17))

# print(lru)


