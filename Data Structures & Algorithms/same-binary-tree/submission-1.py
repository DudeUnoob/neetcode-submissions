# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        pStack = []
        qStack = []

        def preOrderTraversalP(root):
            if root is None:
                pStack.append(None)
                return
            
            pStack.append(root.val)
            preOrderTraversalP(root.left)
            preOrderTraversalP(root.right)

        preOrderTraversalP(p)

        def preOrderTraversalQ(root):
            if root is None:
                qStack.append(None)
                return
            
            qStack.append(root.val)
            preOrderTraversalQ(root.left)
            preOrderTraversalQ(root.right)    

        preOrderTraversalQ(q)  


        return pStack == qStack

    
         