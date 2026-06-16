# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack2 = []
        stack1 = []

        def pre(root=subRoot):

            if not root:
                stack2.append("#")
                return
            
            stack2.append(root.val)
            pre(root.left)
            pre(root.right)


        pre()

        def pre1(root=root):
            if not root:
                stack1.append("#")
                return

            stack1.append(root.val)
            pre1(root.left)
            pre1(root.right)

        pre1()

        print(stack1, stack2)
        
        
        n = len(stack1)
        m = len(stack2)

        if m > n:
            return False

        for i in range(n - m + 1):
            if stack1[i:i + m] == stack2:
                return True
                
        return False
