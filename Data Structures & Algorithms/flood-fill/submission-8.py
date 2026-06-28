class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        from sr, sc start flood fill
        change it to color for each directly adjacent horizontal or vertically and share the
        same color of the starting pixel
        stop when thre are no more adhacent pixels of the original color to update
            2 2 2
            2 2 0
            2 0 1

         0  0 0 0 0 0 
         0  0 0 0 0 0 
         0  0 0 0 0 0 
         0  0 0 0 0 0 (m + n - 1) * (m + n - 1) approx (m + n) * (m + n) = m2 + 2mn + n2
        """
        if image[sr][sc] == color:
            return image

        visited  = set()
        original_number = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        def traversal(sr, sc):

            if sr < 0 or sc < 0 or sr == rows or sc == cols or (sr, sc) in visited or image[sr][sc] != original_number: 
                return None

            #print(sr, sc, "color", image[sr][sc])
            image[sr][sc] = color

            visited.add((sr, sc))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                traversal(sr + dx, sc + dy)
            
        traversal(sr, sc)
        return image