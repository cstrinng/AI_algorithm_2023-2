
from unittest import defaultTestLoader


class Node:
    pass

class Iterator:
    def __init__(self, first:Node):
        self.cur = first

class LinkedList:
    def __init__(self):
        self.first = None
        
    def isEmpty(self) -> bool:
        return (self.fitst is None)

    def getIterator(self) -> Iterator:
        return Iterator(self.first)
    
    def atEnd(self) -> bool:
        return self.cur is None
    
    def getData(self) -> int:
        if self.atEnd():
            #error
            return 0
        return self.cur.data

    def InsertAfter(self, x:int):
        if self.atEnd(): return
        newnode = Node()
        newnode.data = x
        newnode.next = self.cur.next
        self.cur.next = newnode


LList = LinkedList()

i = list.getIterator()

while not i.atEnd():
    print(i.getData())
    i.next()