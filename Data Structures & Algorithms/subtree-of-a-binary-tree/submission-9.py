class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        rootStack = []

        def preOrder(root=root):
            if root is None:
                return rootStack.append("")

            rootStack.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        
        preOrder()


        subRootStack = []
        def preOrderSub(root=subRoot):
            if root is None:
                return subRootStack.append("")

            subRootStack.append(root.val)
            preOrderSub(root.left)
            preOrderSub(root.right)


        preOrderSub()

        print(rootStack)
        print(subRootStack)

        for i in range(len(rootStack) - len(subRootStack) + 1):
            window = rootStack[i:i + len(subRootStack)]

            if window == subRootStack:
                return True

        return False










        