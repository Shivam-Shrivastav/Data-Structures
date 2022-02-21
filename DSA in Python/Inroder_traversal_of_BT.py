class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorderTraversal(node):
    if node:

        inorderTraversal(node.left)
        print(node.value)
        inorderTraversal(node.right)

def preTraversal(node):
    if node:
        print(node.value)
        preTraversal(node.left)
        preTraversal(node.right)

def postTraversal(node):
    if node:
        postTraversal(node.left)
        postTraversal(node.right)
        print(node.value)



if __name__=="__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    print("Preorder traversal of binary tree is")
    preTraversal(node)
    
    print ("\nInorder traversal of binary tree is")
    inorderTraversal(node)
    
    print ("\nPostorder traversal of binary tree is")
    postTraversal(node)
            
