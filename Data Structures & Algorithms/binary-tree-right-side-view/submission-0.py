# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = [root.val]
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        i = len(right)
        ret += right
        if i < len(left):
            ret += left[i:]

        return ret