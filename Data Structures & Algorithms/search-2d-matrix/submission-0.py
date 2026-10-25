class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        
        # return False


        # Real Solution
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while r >= l:
            m = (r + l) // 2
            item = matrix[m // cols][m % cols]
            if item == target:
                return True
            elif item > target:
                r = m - 1
            else:
                l = m + 1
        
        return False