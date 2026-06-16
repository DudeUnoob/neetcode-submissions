# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        stack = [root]

        while stack:

            node = stack.pop()

            

            if node.left and node.right:

                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

            elif node.right and node.left is None:

                stack.append(node.right)

                node.left, node.right = node.right, node.left

            elif node.left and node.right is None:

                stack.append(node.left)

                node.right, node.left = node.left, node.right
            
        return root
          