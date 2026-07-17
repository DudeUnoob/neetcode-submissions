from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connections = defaultdict(list)

        for u, v in edges:

            connections[u].append(v)
            connections[v].append(u)


        visited = set()

        

        

        total = 0

        for i in range(n):

            if i in visited:
                continue

            visited.add(i)
            queue = deque([i])

            while queue:

                node = queue.popleft()

                for neighbor in connections[node]:

                    if neighbor not in visited:

                        visited.add(neighbor)
                        queue.append(neighbor)

            
            total += 1

        
        return total





