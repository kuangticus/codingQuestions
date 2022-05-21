'''
Binary Tree class implementation:
'''
class BST():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                        self.right = node(data)
                else:
                    self.right.insert(data)                    
        else:
            self.data = data
            
    def PrintTree(self):

        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
