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

        left = 0 
        right = (rows * cols) - 1

        while right >= left:
            mid = (right + left) // 2
            item = matrix[mid // cols][mid % cols]
            if item == target:
                return True
            elif item > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

