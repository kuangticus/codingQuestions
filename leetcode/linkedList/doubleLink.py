'''
Double linked list implemenation:
    -addFront(val): adds value to front of list O(1)
    -addBack(val): adds value to end of list O(1)
    -removeIndex(index): removes specified index O(N)
    -display(): prints the current list
    -removeIndex(index): removes things based on index
    -getLength(): gets the length of the list
    -findEle(val): returns the index of element
'''

class node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class doubleLink:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def addFront(self, val):
        if self.head == None:
            new = node(val, None, None)
            self.head = new
            self.tail = new
        else:
            new = node(val, self.head, None)
            self.head.prev = new
            self.head = new
        self.length += 1
    def addBack(self, val):
        if self.head == None:
            new = node(val, None, None)
            self.head = new
            self.tail = new
        else:
            new = node(val,None, self.tail)
            self.tail.next = new
            self.tail = new
        self.length += 1
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.val, end= " ")
            temp = temp.next
        print()
    def removeIndex(self, i):
        if i+1 > self.length:
            return False
        if i == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        else:
            temp = self.head
            for i in range(i):
                temp = temp.next
            if temp.next == None:
                temp.prev.next = None
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev.next
            self.length -= 1
    def getLength(self):
        return self.length
    def rvsList(self):
        temp = self.tail
        while temp:
            print(temp.val, end=" ")
            temp = temp.prev    
        print("")   
    def findEle(self, val)->int:
        i = 0
        temp = self.head
        while temp:
            if temp.val == val:
                return i
            temp = temp.next
            i += 1 
        return None