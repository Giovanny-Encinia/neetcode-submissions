class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        suma = 0
        # sum the first row
        for j in range(len(matrix[0])):
            suma += matrix[0][j]
            prefix_sum[0][j] = suma

        suma = 0
        # sum the first column
        for i in range(len(matrix)):
            suma += matrix[i][0]
            prefix_sum[i][0] = suma

        # fill the rest of the matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                prefix_sum[i][j] = matrix[i][j] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]
        
        self.prefix_sum = prefix_sum
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            diagonal_area = self.prefix_sum[row1 - 1][col1 - 1]
        else:
            diagonal_area = 0

        if row1 > 0:
            top_area = self.prefix_sum[row1 - 1][col2]
        else:
            top_area = 0
        
        if col1 > 0:
            left_area = self.prefix_sum[row2][col1 - 1]
        else:
            left_area = 0

        total_area = self.prefix_sum[row2][col2]
        
        return total_area + diagonal_area - top_area - left_area
        
        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)