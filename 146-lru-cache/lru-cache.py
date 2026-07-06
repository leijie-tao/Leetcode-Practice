# Use hashmap to store the key and the node. ——> Find the target node by key.
# Linked list maintain the order. ——> Find the least recently used node.
class Node:  
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None        #Create doubly-linked list with pre/next pointers.
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # Create an empty linked list with virtual head/tail nodes to track the real head(head.next) and real tail(tail.prev)
        self.head = Node()           #virtual node
        self.tail = Node()           #virtual node
        self.head.next = self.tail   
        self.tail.prev = self.head




    # Remove a node: Link the previous one with the next one.
    def remove(self, node): 
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert : Add a node in front of whole list and behind the virtual head nodes
    def insert(self, node): 
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node




    # Get: take the node out, add it to the front, and return the node.val
    def get(self, key: int) -> int: 
        if key not in self.map:
            return -1
        self.remove(self.map[key])
        self.insert(self.map[key])
        return self.map[key].val

    
    def put(self, key: int, value: int) -> None:
        # If the node exists, update the value and position.
        if key in self.map:               
            self.map[key].val = value 
            self.remove(self.map[key])
            self.insert(self.map[key])
        # Otherwise, record the node and add it to the front.
        else:                           
            self.map[key] = Node(key, value)
            self.insert(self.map[key])
            # Also check the capacity. Remove the tail.prev when overload.
            if len(self.map) > self.capacity:
                last_node = self.tail.prev
                self.remove(last_node)
                del self.map[last_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)