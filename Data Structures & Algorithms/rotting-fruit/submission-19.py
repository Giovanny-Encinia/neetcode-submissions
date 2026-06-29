from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        total_fresh = 0
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total_fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
      
        level = 0
        while total_fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        total_fresh -= 1
                       
            level += 1
        
        return level if total_fresh == 0 else -1
