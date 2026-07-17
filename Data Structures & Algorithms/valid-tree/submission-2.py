from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        if len(edges) != (n - 1):
            return False

        connections = defaultdict(set)

        for u, v in edges:

            connections[u].add(v)
            connections[v].add(u)

        visited = set()


        def dfs(node):

            if node in visited:
                return False

            visited.add(node)

            for neighbor in list(connections[node]):
                connections[neighbor].discard(node)
                
                if not dfs(neighbor):
                    return False

            return True

        
        return dfs(0) and len(visited) == n

                

        