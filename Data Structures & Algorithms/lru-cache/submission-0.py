class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # to allow fast lookup of nodes
        self.cap = capacity

        self.dummyLeft, self.dummyRight = Node(0, 0), Node(0, 0)
        self.dummyLeft.next, self.dummyRight.prev = self.dummyRight, self.dummyLeft        

    def remove(self, Node):
        # destroy the link of Node with its previous and next nodes and 
        # link prev and next nodes of Node
        nxt, prev = Node.next, Node.prev
        prev.next, nxt.prev = nxt, prev

    def insert(self, Node):
        # add the Node right before self.dummyRight
        prev, nxt = self.dummyRight.prev, self.dummyRight
        Node.next, Node.prev = nxt, prev
        prev.next, nxt.prev = Node, Node

    def get(self, key: int) -> int:
        # get value and update so that it becomes the MRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # update if exists, if not add
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            # delete the next node of dummyLeft, LRU
            del self.cache[self.dummyLeft.next.key]
            self.remove(self.dummyLeft.next)
