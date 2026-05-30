# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        l = r = 0
        if not root:
            return True
        if root.left:
            l = self.depth(root.left)
        if root.right:
            r = self.depth(root.right)
        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def depth(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        else:
            l = r = 0
            if root.left:
                l = 1 + self.depth(root.left)
            if root.right:
                r = 1 + self.depth(root.right)
            return max(l, r)
