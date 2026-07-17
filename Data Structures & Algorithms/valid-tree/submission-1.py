from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        if len(edges) != n - 1:
            return False

        
        connections = defaultdict(list)

        for u, v in edges:

            connections[u].append(v)
            connections[v].append(u)


        visited = set()


        def dfs(node):

            if node in visited:
                return False

            visited.add(node)

            for neighbor in connections[node]:

                if node in connections[neighbor]:
                    connections[neighbor].remove(node)

            
                if not dfs(neighbor):
                    return False

            return True

        
        return dfs(0) and len(visited) == n

    
