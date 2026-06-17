class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUcache:
    def __init__(self, capacity:int):
        self.size = 0
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def contains(self, key:int):
        return key in self.map
    
    def put(self, key:int, val:int):
        if(self.size == self.capacity):
            d = self.head.next
            del self.map[d.key]
            self.delNode(d)
        x = Node(key, val)
        self.map[key] = x
        self.addNode(x)
        if self.size < self.capacity:
            self.size += 1
    
    def get(self, key:int):
        x = self.map[key]
        self.delNode(x)
        self.addNode(x)
        return x.val
    
    def addNode(self, x:Node):
        p = self.tail.prev
        x.next = p.next
        x.prev = p
        p.next.prev = x
        p.next = x

    def delNode(self, x:Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        x.next = None
        x.prev = None
    
    def clear(self):
        self.size = 0
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head