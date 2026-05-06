# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        def preOrder(root):
            if root is None:
                return None

            stack.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)
        print(stack)

        stack.sort()

        return stack[k - 1]


            