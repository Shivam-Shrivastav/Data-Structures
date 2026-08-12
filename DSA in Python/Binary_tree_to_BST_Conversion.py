#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def inorder_tree(self, root, arr):
        if not root:
            return
        self.inorder_tree(root.left, arr)
        arr.append(root.data) 
        self.inorder_tree(root.right, arr)
    
    def inorder_bst(self, root, arr):
        if not root:
            return
        self.inorder_bst(root.left, arr)
        root.data = arr[0]
        arr.pop(0)
        self.inorder_bst(root.right, arr)
    def binaryTreeToBST(self, root):
        # code here
        arr = []
        self.inorder_tree(root, arr)
        arr.sort() # sorted array is the inorder BST
        self.inorder_bst(root, arr) # Putting element of arr in inorder fashion to form a BST
        
        return root

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def printInorder(root): 
    if root is None: 
        return
    printInorder(root.left) 
    print (root.data, end=' ')  
    printInorder(root.right) 

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        Solution().binaryTreeToBST(root)
        printInorder(root)
        print()
# } Driver Code Ends