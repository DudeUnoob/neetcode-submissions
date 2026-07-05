from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        distance = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.popleft()
                grid[r][c] = distance

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == INF and
                        (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            distance += 1