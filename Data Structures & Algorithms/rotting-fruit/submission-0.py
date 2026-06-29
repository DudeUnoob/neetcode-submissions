from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        res = 0
        queue = deque()

        visited = set()


        for r in range(ROWS):
            for c in range(COLS):
                
                if (r, c) in visited:
                    continue
                if grid[r][c] == 2:
                    queue.append((r, c))

                if grid[r][c] == 1:
                    fresh += 1


        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:

            size = len(queue)

            for _ in range(size):

                node = queue.popleft()

                r, c = node[0], node[1]


                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1

            res += 1

                
                    
        return res if fresh == 0 else -1




