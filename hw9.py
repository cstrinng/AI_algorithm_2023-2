class Tree:
    def __init__(self):
        self.root = 1
        
    def doInorderTraversal(self, r):
        if list[r] is None: return

        self.doInorderTraversal(2*r)
        print(list[r])
        list[r] = None
        self.doInorderTraversal(2*r+1)
        
    def inorderTraversal(self):
        self.doInorderTraversal(self.root)
        

n = int(input())
list = [None for i in range(2*n+2)]
for i in range(n):
    list[i+1] = input()
    
#for i in range(2*n+1):
#    print(list[i])


MyTree = Tree()
MyTree.inorderTraversal()