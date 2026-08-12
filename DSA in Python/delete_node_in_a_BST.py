# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def insucc(self, root):
        p = root.right
        while p.left:
            p = p.left
        return p
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                temp = root.left
                del root
                return temp
            elif not root.left:
                temp = root.right
                del root
                return temp
            else:
                temp = self.insucc(root)
                temp.val, root.val = root.val, temp.val
                root.right = self.deleteNode(root.right, key)
        return root
            
        
        
        