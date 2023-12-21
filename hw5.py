
class Node:
    def __init__(self):
        self.next = None
    def data(self):
        return self
    

class LinkedList:
    def __init__(self):
        self.first = self.last = None
        
    def isEmpty(self) -> bool:
        return (self.first is None)
    
    def DeleteFirst(self) -> int:
        if self.first is None: return -1
        ret = self.first.data
        self.first = self.first.next
        return ret
    
    def InsertAtEnd(self, x:int):
        newnode = Node()
        newnode.data = x
        if self.first is None:
            self.first = self.last = newnode
        else: 
            self.last.next = newnode
            self.last = newnode

    def DisplayAll(self):
        cur = self.first
        while cur is not None:
            print(cur.data)
            cur = cur.next
            

class Queue:
    def __init__(self):
        self.llist = LinkedList()        
        
    def enqueue(self, x:int) -> int:
        self.llist.InsertAtEnd(x)
        return 0
        
    def dequeue(self) -> int:
        if self.llist.first is None:
            return -1
        else:
            ret = self.llist.first.data
            self.llist.DeleteFirst()
            return ret
    

Q = Queue()

n = int(input())
for i in range(n):
    operate = input()
    if operate[:3] == 'deq':
        print(Q.dequeue())
    elif operate[:3] == 'enq':
        o, x = operate.split()
        x = int(x)
        print(Q.enqueue(x))