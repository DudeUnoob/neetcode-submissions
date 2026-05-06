class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preOrderTraversal(node):
            if node is None:
                return [""]

            return [f"{node.val}"] + preOrderTraversal(node.left) + preOrderTraversal(node.right)

        
        stack1 = preOrderTraversal(root)
        stack2 = preOrderTraversal(subRoot)

        n, m = len(stack1), len(stack2)

        for i in range(n - m + 1):
            if stack1[i:i+m] == stack2:
                return True

        return False












        