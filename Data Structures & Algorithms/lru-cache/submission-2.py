class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None
    
# Doubly linked list
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {} # fast lookups

        self.left, self.right = Node(0, 0), Node(0, 0) # dummy
        self.left.next, self.right.prev = self.right, self.left

    # insert new key-value right behind the right dummy pointer
    def insert(self, key: int, value: int) -> None:
        node = Node(key, value)
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, self.right

        self.cache[key] = node
        self.count += 1
    
    def remove(self, key: int) -> None:
        nodeToRemove = self.cache[key]
        del self.cache[key]

        prev, nxt = nodeToRemove.prev, nodeToRemove.next
        prev.next, nxt.prev = nxt, prev
        self.count -= 1

    def get(self, key: int) -> int:
        if key not in self.cache: # key does not exist
            return -1
        
        # remove and reinsert to make it the most recently used
        node = self.cache[key]
        self.remove(key)
        self.insert(node.key, node.val) 
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node.key)
            node.val = value
            self.insert(node.key, node.val)
            return

        node = Node(key, value)
        self.insert(node.key, node.val)
        if self.count > self.capacity: # if we exceed the capacity, remove the lru
            lru = self.left.next
            self.remove(lru.key)


