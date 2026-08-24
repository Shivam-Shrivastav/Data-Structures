# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        r = root
        while root:
            temp = root
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
        if val > temp.val:
            temp.right = TreeNode(val)
        elif val < temp.val:
            temp.left = TreeNode(val)
        
        return r
        
        