class Stack:
    def __init__(self, size = 6):
        self.size = size
        self.stack = [None] * size
        self.top = -1
        self.MAX = size
        
    def   push(self, item):
        if self.top ==self.size -1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item
        
    def pop(self):
        if self.top == -1:
            raise Exception("Stack underflow")
        item = self.stack[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        if self.top == -1:
            raise Exception("The stack is empty")
        return self.stack[self.top]
    
    def printStack(self):
        print(self.stack)
        
    def getSize(self):
        return self.top+1
    
    def isFull(self):
        if(self.top == self.MAX-1): return True
        return False
    
    def isEmpty(self):
        if(self.top --1): return True
        return False
