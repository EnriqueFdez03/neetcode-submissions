class Node:
    def __init__(self, key, val, nextNode = None, prevNode = None):
        self.val, self.key = val, key
        self.next, self.prev = nextNode, prevNode

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.numItems = 0
        self.keyToNode = {}
        self.dummyLeft, self.dummyRight = Node(0,0), Node(0,0)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def delete(self, key):
        if key not in self.keyToNode:
            return
        
        node = self.keyToNode[key]
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        del self.keyToNode[key]
        self.numItems -= 1
    
    def insert(self, key, value):
        prev, nxt = self.dummyRight.prev, self.dummyRight
        node = Node(key, value, nxt, prev)
        nxt.prev = node
        prev.next = node
        self.keyToNode[key] = node
        self.numItems += 1

    def get(self, key: int) -> int:
        if not key in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        self.delete(key)
        self.insert(node.key, node.val)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.delete(key)

        # insert the node
        self.insert(key, value)

        # if capacity exceeds delete the lru
        if self.numItems > self.capacity:
            prev, nxt = self.dummyLeft, self.dummyLeft.next
            second = nxt.next
            self.delete(nxt.key)
            prev.next = second