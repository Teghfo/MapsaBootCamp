class Element:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def addBegin(self, newElement):
        if self.root == None:
            self.root = newElement
        else:
            newElement.next = self.root
            self.root = newElement

        self.length += 1

    def addEnd(self, newElement):
        pass

    def addBet(self, oldElement, newElement):
        pass

    def remElem(self, element):
        pass

    def printLinkedList(self):
        if self.root == None:
            print('Empty!')

        else:
            temp = self.root
            print(temp.name)
            while(temp.next):
                temp = temp.next
                print(temp.name)


l = LinkedList()

elm1 = Element('ashkan')
elm2 = Element('Arash')
elm3 = Element('Ali')


l.addBegin(elm1)
l.addBegin(elm2)
l.addBegin(elm3)

l.printLinkedList()
