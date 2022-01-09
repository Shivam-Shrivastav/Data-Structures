from types import new_class


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def insertAfter(self, prevnode, data):
        newnode = Node(data)
        if prevnode == None:
            print("Previous node cant be null")
            return
        else:
            newnode.next = prevnode.next
            prevnode.next = newnode
    def append(self, data):
        newnode = Node(data)
        last = self.head
        if self.head == None:
            self.head = newnode
            return
        
        while(last.next):
            last = last.next
        
        last.next = newnode
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
def main():
    l1 = LinkedList()
    l1.push(7)
    l1.push(6)
    l1.push(5)
    l1.append(4)
    l1.push(2)
    l1.insertAfter(l1.head.next.next,3)
    l1.push(1)
    l1.printList()

if __name__ == "__main__":
    main()
