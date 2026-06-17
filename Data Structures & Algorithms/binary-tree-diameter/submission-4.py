class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        self.res = 0


        def dfs(root=root):

            if not root:
                return 0

            #get height of left subtree
            left = dfs(root.left)
            
            # get height of right subtree
            right = dfs(root.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)
            

        dfs()


        
        return self.res