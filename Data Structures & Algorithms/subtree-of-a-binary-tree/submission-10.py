# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False

        rootStack, subRootStack = [], []

        def preOrder(node):
            if node is None:
                rootStack.append('null')
                return
            rootStack.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        def preOrderSub(node):
            if node is None:
                subRootStack.append('null')
                return
            subRootStack.append(node.val)
            preOrderSub(node.left)
            preOrderSub(node.right)

        preOrder(root)
        preOrderSub(subRoot)

        print(rootStack)   # now this will run
        print(subRootStack)

        

        n, m = len(rootStack), len(subRootStack)
        for i in range(len(rootStack) - len(subRootStack) + 1):

            if rootStack[i:i + m] == subRootStack:
                return True

        return False

       


            