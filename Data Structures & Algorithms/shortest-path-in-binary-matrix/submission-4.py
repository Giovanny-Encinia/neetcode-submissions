from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()

        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        queue.append((0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = set()
        visited.add((0,0))
        length = 1
        rows, cols = len(grid), len(grid[0])
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                for dr, dc in directions:
                    if (r + dr < 0 or c + dc < 0
                        or r + dr == rows or c + dc == cols or
                        ((r + dr, c + dc)) in visited or 
                        grid[r + dr][c + dc] == 1
                        ):
                        continue 
                    visited.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
            length += 1
        return -1
