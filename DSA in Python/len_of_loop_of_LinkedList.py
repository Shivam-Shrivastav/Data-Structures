#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    # To find the length of the loop firstly we have to find the starting  point of the loop
    #Let
    count = 0
    slow = head
    fast = head
    while slow!=None and fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow==fast: # There loop exist
            count = 1  
            break
    # Now we are finding starting point of the loop and we will bring
    # the both slow and fast pointer on it and will run the slow pointer with 1
    #step till it reach the fast pointer again and we will add 1
    #to count in each step
    # Hence we will find the length of the loop of the linked list
    if slow == head:
        while fast!=slow:
            fast =fast.next
        slow = slow.next
        while slow!=fast:
            slow = slow.next
            count = count + 1
        
        
    
    elif slow==fast:
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        slow = slow.next
        while slow!=fast:
            slow = slow.next
            count = count + 1
    
    return count
        
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(countNodesinLoop(LL.head))

# } Driver Code Ends