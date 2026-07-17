from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        pac = set()
        atl = set()

        def bfs(queue):
            visited = set(queue)
            
            while queue:

                r, c = queue.popleft()

                for dr, dc in directions:

                    newR = r + dr
                    newC = c + dc

                    if (

                        0 <= newR < ROWS and 
                        0 <= newC < COLS and
                        (newR, newC) not in visited
                        and heights[newR][newC] >= heights[r][c]
                    ):
                        visited.add((newR, newC))
                        queue.append((newR, newC))

            return visited

        
        pacificQueue = deque()
        atlanticQueue = deque()

        for r in range(ROWS):

            pacificQueue.append((r, 0))
            atlanticQueue.append((r, COLS - 1))

        for c in range(COLS):

            pacificQueue.append((0, c))
            atlanticQueue.append((ROWS - 1, c))

        pacific = bfs(pacificQueue)
        atlantic = bfs(atlanticQueue)

        result = []

        for r in range(ROWS):
            for c in range(COLS):

                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result

