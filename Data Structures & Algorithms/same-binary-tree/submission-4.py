# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stackP = []
        stackQ = []


        def preTravP(root=p):

            if not root:
                stackP.append("")
                return

            stackP.append(root.val)
            preTravP(root.left)
            preTravP(root.right)


        def preTravQ(root=q):

            if not root:
                stackQ.append("")
                return

            stackQ.append(root.val)
            preTravQ(root.left)
            preTravQ(root.right)

        preTravP()
        preTravQ()

        return stackP == stackQ
            