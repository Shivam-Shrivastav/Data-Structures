import Create_And_Insertion_In_LinkedList

def reverseList(self):
        prev = None
        next = None
        curr = self.head
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

l1 = Create_And_Insertion_In_LinkedList.LinkedList()

l1.push(3)
l1.push(2)
l1.push(1)
reverseList(l1)
l1.printList()


