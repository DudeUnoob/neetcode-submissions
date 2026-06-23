from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connections = defaultdict(list)

        
        for i in range(len(edges)):

            a, b = edges[i][0], edges[i][1]
            
            connections[a].append(b)
            connections[b].append(a)

        print(connections)
        

        visited = set()
        


        def dfs(node):

            visited.add(node)
            


            for neighbor in connections[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            

            return



        
        res = 0

        for key in range(n):

            if key not in visited:
                res += 1
                dfs(key)
        return res