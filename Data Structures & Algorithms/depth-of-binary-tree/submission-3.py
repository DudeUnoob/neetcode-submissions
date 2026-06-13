# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
count = 0

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        
        if not root:
            return count
        
        


        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1