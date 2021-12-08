class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
        
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print("\n",printval.data,)
            printval = printval.next
            print()


llist = SLinkedList()
llist.head=Node("Front")
e2=Node("Mon")
e3=Node("Tues")
e4=Node("wed")
e5=Node("fri")

llist.head.next = e2
e2.next=e3
e3.next=e4
e4.next=e5

while True:
    print("[a]add node to front\n[b]add to end\n[c]add at middle\n[d]remove\n[e]exit")
    choice = input("Choice: ")
    if choice in "aA":
        b = input("Node to input @ front: ")
        llist.Atbegining(b)
        llist.LListprint()
    elif choice in "Bb":
        b = input("Node to input @ end: ")
        llist.AtEnd(b)
        llist.LListprint()
    elif choice in "Cc":
        b = input("Node to input @ middle: ")
        llist.Inbetween(llist.head.next, b)
        llist.LListprint()
    elif choice in "Dd":
        b = input("Node to remove: ")
        llist.RemoveNode(b)
        llist.LListprint()
    elif choice in "Ee":
       break
