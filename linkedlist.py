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
            


        
LList = LinkedList()
LList.InsertAtEnd(4)
LList.DisplayAll()
LList.InsertAtEnd(5)
LList.DisplayAll()
LList.InsertAtEnd(6)
LList.DisplayAll()
LList.DeleteFirst()
LList.DeleteFirst()
LList.DeleteFirst()
LList.DisplayAll()
print(LList.isEmpty())


