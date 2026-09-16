from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        queue = deque()
        
        fresh = 0
        time = 0

        directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        for r in range(ROWS):

            for c in range(COLS):

                if grid[r][c] == 1:

                    fresh += 1

                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue and fresh > 0:

            size = len(queue)

            for _ in range(size):

                r, c = queue.popleft()

                for dr, dc in directions:

                    if 0 <= dr + r < ROWS and 0 <= dc + c < COLS and grid[dr + r][dc + c] == 1:
                        grid[dr + r][dc + c] = 2
                        queue.append((dr + r, dc + c))
                        fresh -= 1


            time += 1


        


        return time if fresh == 0 else -1


