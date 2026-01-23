class Node:  #创建doubly-linked list双向指针pre/next，通过prev指针在O(1)时间删除指定节点
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # 虚拟头尾节点，用于定位最新（头）和最旧（尾），同时保证真实节点都在中间
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int: #每次获取节点，则把它从原位置拿出，并最新到虚拟头节点后
        if key not in self.map:
            return -1
        self.remove(self.map[key])
        self.insert(self.map[key])
        return self.map[key].val

    def remove(self, node): #删除节点，跨过当前节点连接前后节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node): #把节点插入虚拟头节点后面（最新位置）
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def put(self, key: int, value: int) -> None:
        if key in self.map:               #key已存在，则更新值，同时把节点移动到虚拟头节点后
            self.map[key].val = value 
            self.remove(self.map[key])
            self.insert(self.map[key])
        else:                           #不存在则添加新的节点放入最新位置，若超容量则移动尾部节点并删除其key
            self.map[key] = Node(key, value)
            self.insert(self.map[key])
            if len(self.map) > self.capacity:
                last_node = self.tail.prev
                self.remove(last_node)
                del self.map[last_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)