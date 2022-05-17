#LRU with list instead of linked list
#Adpation without using the linked list

class knowledge():

    def __init__(self) -> None:
        self.readList = {} # dictionary for read books
        self.orderList = [] # order of the read books

    def put(self, bookname) -> None:
        if bookname not in self.readList:
            self.readList[bookname] = True
            self.orderList.append(bookname)
        else:
            cur = 0
            for  i, book in enumerate(self.orderList):
                if book == bookname:
                   cur = i 
                   break
            toFront = self.orderList.pop(i)
            self.orderList.insert(0, toFront)

    def get(self) -> None:
        print(self.orderList)

# kw = knowledge()

# kw.put(9)
# kw.put(1)
# kw.put(3)
# kw.put(4)
# kw.put(4)
# kw.put(3)

# print(kw.get())