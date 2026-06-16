# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        if not root:
            return []

        queue = deque([root])
        result = []


        while queue:

            current_level = []

            for _ in range(len(queue)):

                node = queue.popleft()

                current_level.append(node.val)


                if node.left:

                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        stack = []

        for i in range(len(result)):

            stack.append(result[i][-1])

        return stack

