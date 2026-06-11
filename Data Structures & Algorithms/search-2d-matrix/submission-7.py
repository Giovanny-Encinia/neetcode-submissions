class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = len(matrix[0])

        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        total = right

        while left <= right:
            mid = (left + right) // 2

            mid_r = mid // size
            mid_c = mid % size

            if matrix[mid_r][mid_c] == target:
                return True

            if target > matrix[mid_r][mid_c]:
                left = mid + 1
            else:
                right = mid - 1

        return False 