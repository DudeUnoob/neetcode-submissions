# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = []


        def inOrder(root):
            if root is None:
                return []

            inOrder(root.left)
            stack.append(root.val)
            inOrder(root.right)


        inOrder(root)

        for i in range(1, len(stack)):
            if stack[i] <= stack[i - 1]:
                return False

        return True
            