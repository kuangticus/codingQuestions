def stack():
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
    
    def getStack(self):
        return self.items

    