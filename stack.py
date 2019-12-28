class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if len(self.stack) == 0:
            print("Nothing To Pop \n")
        else:
            self.stack = self.stack[:-1]
            
    def last(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)


x = Stack()
x.push(10)
print(x.length())
print(x.last())
x.push(20)
print(x.length())
print(x.last())
x.pop()
print(x.length())
print(x.last())
x.pop()
x.pop()
