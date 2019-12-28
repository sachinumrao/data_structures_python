class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if len(self.stack) == 0:
            print("Nothing To Pop \n")
        else:
            x = self.stack[-1]
            self.stack = self.stack[:-1]
            return x
            
    def last(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)

def main():
    pass
    
if __name__ == "__main__":
    main()