class Node :
    def __init__(self,key=0,value=0):
        self.key = key 
        self.value = value 
        self.prev = None
        self.next = None
        self.freq = 1
class DLL :
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.next

    def addNode(self,node: Node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    def removeNode(node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
    def removeLast(self):
        if self.isEmpty():
            return None
        last = self.tail.prev
        self.removeNode(last)
        return last
    def isEmpty(self):
        return self.head.next == self.tail
class LFU :
    def __init__(self,capacity : int = 10):
        self.keyMap = dict()
        self.freqMap = dict()
        self.capacity = capacity
        self.minFreq = 0
    def updateFreq(self,node: Node):
        dll = self.freqMap[node.freq]
        dll.remove(node)
        if dll.isEmpty() and node.freq == self.minFreq:
            self.minFreq += 1
        node.freq += 1
        if node.freq not in self.freqMap:
            self.freqMap.setdefault(node.freq,DLL())
        dll = self.freqMap[node.freq]
        dll.addNode(node)
    def get(self,key: int):
        if not self.keyMap.get(key):
            return -1
        node = self.keyMap.get[key]
        self.updateFreq(node)
        return node.value
    def put(self,key,value):
        if self.keyMap.get(key):
            node = self.keyMap.get(key)
            node.value = value
            self.updateFreq(node)

        if self.capacity == 0:
            dll = self.freqMap[self.minFreq]
            toremove = dll.removeLast()
            self.keyMap.pop(toremove.key)
            self.capacity += 1
        
        newNode = Node(key,value)
        self.minFreq = 1
        if not self.freqMap.get(1):
            self.freqMap.setdefault(1,DLL())
        self.freqMap.get(1).addNode(newNode)
        self.keyMap[key] = node