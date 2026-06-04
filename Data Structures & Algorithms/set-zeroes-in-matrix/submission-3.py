class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    #print("iszero")
                    up = down = right = left = 0

                    while i - up >= 0:
                        if matrix[i - up][j] != 0:
                            matrix[i - up][j] = None
                        up += 1
                    
                    while i + down < len(matrix):
                        if matrix[i + down][j] != 0:
                            matrix[i + down][j] = None
                        down += 1
                    
                    while j + right < len(matrix[0]):
                        if matrix[i][j + right] != 0:
                            matrix[i][j + right] = None
                        right += 1
                    
                    while j - left >= 0:
                        if matrix[i][j - left] != 0:
                            matrix[i][j - left] = None
                        left += 1
                    
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
        
