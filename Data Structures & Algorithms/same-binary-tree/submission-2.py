# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        pS, qS = [], []

        def pT(root=p):
            
            if root is None:
                pS.append(None)
                return None

            pS.append(root.val)
            pT(root.left)
            pT(root.right)

        def qT(root = q):

            if root is None:
                qS.append(None)
                return None

            qS.append(root.val)
            qT(root.left)
            qT(root.right)

        pT()
        qT()

        return pS == qS

    
         