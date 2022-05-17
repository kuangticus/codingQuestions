'''
Linked List Implementation:
Function:
    -addFront(val): adds an element to the front of list O(1)
    -addBack(val): adds an elements to the end of list O(1)
    -display(): displays the current linked list O(N)
    -removeIndex(index): removes the specified index from list O(N)
    -getLength(): gets the length of linked list
    -findEle(val): returns the index where val is at else -1 O(N)
'''

class node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next
class singleLL:
    def __init__(self) -> None:
        self.head = None    
        self.tail = None
        self.length = 0
    def addFront(self, val):
        #if we just starting out
        if self.head == None :
            temp = node(val, None)
            self.head = temp
            self.tail = temp
        else:
            temp = node(val, self.head)
            self.head = temp
        self.length += 1
    def addBack(self, val):
        if self.head == None :
            temp = node(val, None)
            self.head = temp
            self.tail = temp
        else:
            temp = node(val, None)
            self.tail.next = temp
            self.tail = temp
        self.length += 1
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()
    def removeIndex(self, i):
        if i+1 > self.length:
            return False
        if i == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            temp = self.head
            for i in range(i-1):
                temp = temp.next
            if temp.next.next == None:
                temp.next = None
            else:
                temp = temp.next.next
            self.length -= 1  
    def getLength(self):
        return self.length          
    def findEle(self, val)->int:
        i = 0
        temp = self.head
        while temp:
            if temp.val == val:
                return i
            temp = temp.next
            i += 1 
        return None
