#{ 
#Driver Code Starts
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
    

 # } Driver Code Ends
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
    count= None
    def search_node(self, ele, root):
        if root is None or root.data == ele:
            return root
        elif ele < root.data:
            return self.search_node(ele, root.left)
        elif ele > root.data:
            return self.search_node(ele, root.right)
            
    def inorder(self, root, arr, x):
        if not root:
            return
        self.inorder(root.left, arr, x)
        if self.search_node(x-root.data, arr):
            Solution.count+=1
        self.inorder(root.right, arr, x)

    def countPairs(self, root1, root2, x): 
        #code here.
        Solution.count = 0
        self.inorder(root1, root2, x)
        
        return Solution.count
                
        
        

#{ 
#Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        root1=buildTree(s1)
        root2=buildTree(s2)
        x=int(input())
        ob = Solution()
        print(ob.countPairs(root1,root2,x))
#} Driver Code Ends