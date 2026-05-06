# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        def inOrder(root=root):

            if root is None:
                return

            inOrder(root.left)
            stack.append(root.val)
            inOrder(root.right)

        inOrder()

        print(stack)


        count = 0

        while stack:
            smallest = min(stack)
            stack.remove(smallest)
            count += 1

            if count == k:
                return smallest

        return None
