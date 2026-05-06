# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_stack, q_stack = [], []

        def pPreOrder(root=p):

            if not root:
                p_stack.append("null")
                return

            p_stack.append(root.val)
            pPreOrder(root.left)
            pPreOrder(root.right)

        pPreOrder()

        def qPreOrder(root=q):

            if not root:
                q_stack.append("null")
                return

            q_stack.append(root.val)
            qPreOrder(root.left)
            qPreOrder(root.right)


        qPreOrder()


        return p_stack == q_stack