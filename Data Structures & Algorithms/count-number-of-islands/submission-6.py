class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1 0
        0 1

        if current is 1 and left, right, top, bottom is 0 then island

        0 1 0 
        1 1 1
        0 1 0

        link items in matrix to create bigger islands

        definition of a island

        four directions
        """
        count_islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def traversal(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == '0' or (r, c) in visited:
                return None
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            #print(r, c, grid[r][c])
            visited.add((r, c))

            for dx, dy in directions:
                traversal(r + dx, c + dy)
            



        for r, row in enumerate(grid):
            for c, item in enumerate(row):
                if item == '0' or (r, c) in visited:
                    continue
                else:
                    traversal(r, c)
                    count_islands += 1
        
        return count_islands