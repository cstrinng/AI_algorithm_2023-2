from collections import deque
from telnetlib import DO

class Stack:
    def __init__(self):
        self.dq = deque()

    def push(self, x:int):
        self.dq.append(x)
    
    def pop(self) -> int:
        return self.dq.pop()
    
    def isEmpty(self) -> bool:
        return len(self.dq) == 0
 
def  doParenthesesMatch(s:str) -> bool:
        leftp = Stack()
        for c in s :
            if c == '(' or c == '{' or c == '[':
                 leftp.push(c)
            elif c == ')':
                if leftp.isEmpty() or leftp.pop() != '(':
                     return False
            elif c == '}':
                if leftp.isEmpty() or leftp.pop() != '{':
                    return False
            elif c == ']':
                if leftp.isEmpty() or leftp.pop() != '[':
                    return False
                
        return leftp.isEmpty()
        

    
a = Stack()

a.push(4)
a.push(2)
print(a.pop())
a.push(6)
while not a.isEmpty():
    print(a.pop())
    

print(doParenthesesMatch('([{}])'))
print(doParenthesesMatch('{)({[]})}'))