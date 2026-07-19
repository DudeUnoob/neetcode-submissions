from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        connections = defaultdict(list)

        for a, b in prerequisites:

            connections[a].append(b)

        
        visited = set()
        rec_stack = set()


        def dfs(node):

            if node in visited:
                return True

            if node in rec_stack:
                return False

            rec_stack.add(node)

            for neighbor in connections[node]:

                if not dfs(neighbor):
                    return False

                
            rec_stack.remove(node)
            visited.add(node)

            return True


        for course in range(numCourses):

            if not dfs(course):
                return False

        return True

