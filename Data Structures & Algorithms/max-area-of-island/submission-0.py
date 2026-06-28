class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def traversal(r, c):
            
            

            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            count = 1
            visited.add((r, c))
            
            for dx, dy in directions:
                count += traversal(r + dx, c + dy)

            return count

        for r in range(rows):
            for c in range(cols):
                item = grid[r][c]

                if item == 1 and (r, c) not in visited:
                    count_items = traversal(r, c)
                    max_area = max(count_items, max_area)

        return max_area