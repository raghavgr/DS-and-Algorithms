class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty. Cannot pop"
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty. Cannot peek"
        return self.items[-1]
    
    def size(self):
        return len(self.items)

obj = Stack()
obj.push(1)
obj.push(9)
print(obj.peek())