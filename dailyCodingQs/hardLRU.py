# Implementing an LRU/Order Dict from scratch
# Books read, maintaining order move most recently read books to the front of line
# Cheers!

# Amazon Technical Interview question

# Time Complexity: O(N) average for insertion, best case O(1) if element doesn't exist in readlist, Worst Case O(N) value in read list at the end of LL
# Space Complexity: O(N) for dictionary cause it can grow to N books read.
# Technically O(N) for LL + O(N) for Dictionary = O(2N) therefore O(N)

# Class: Book
# Definition: a node that have the book name, variable book name
class Book():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Class: Library
# Definition: Class that houses a linked list for order of books
class Library():

    def __init__(self):
        self.readList = dict()
        self.head = None #head of the linked list
        self.tail = None #tail of the linked list to know where to add to
    
    #Function: put
    #definiion: used to put elements into the linked list
    def put(self, bookname):
        # logic for adding books to ordered list tracked but dictionary 
        if bookname not in self.readList:
            # read list is empty add the first element and start daisy chaining linked list
            if len(self.readList) == 0:
                self.readList[bookname] = True
                self.head = Book(bookname)
                self.head.next = None
                self.tail = self.head
            else: # once there are move than 1 element in readlist we can start adding books into the linked list
                self.readList[bookname] = True
                self.tail.next = Book(bookname)
                self.tail = self.tail.next
        # if the book already has been read/exits in readlist then we move it to the front
        else:
            tempHead = self.head # temphead for re-arranging
            cur = self.head
            prev = None
            next = None

            # linear search linked list for the val and move that node/book to the front
            while cur != None:
                
                # guaranteed to stop on node since we know for a fact it exists
                if cur.val == bookname:
                    if cur != None:
                        next = cur.next
                    break

                prev = cur
                cur = cur.next

            # re-order the list only if the bookname isn't in the front of the list
            if prev and cur:
                self.head = cur
                self.head.next = tempHead
                if next == None:
                    self.tail = prev
                prev.next = next


    def getReadList(self):
        
        move = self.head

        while move != None:
            print(move.val, end =" ")
            move = move.next

# Function testing and calls
# lib = Library()

# lib.put(0)
# lib.put(1)
# lib.put(2)
# lib.put(3)
# lib.put(5)
# lib.put(7)
# lib.put(5)
# lib.put(7)
# lib.put(5)
# lib.put(0)
# lib.put(0)
# lib.put(3)

# print(lib.getReadList())

