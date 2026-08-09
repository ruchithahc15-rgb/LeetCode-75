from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Scan grid to find initial rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If there are no fresh oranges to rot
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Multi-source BFS level by level
        while queue and fresh > 0:
            minutes += 1
            # Process all oranges rotten in the current minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check boundaries and if neighbor is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        fresh -= 1         # Decrement remaining fresh count
                        queue.append((nr, nc))

        # Step 3: Check if all fresh oranges were reachable
        return minutes if fresh == 0 else -1