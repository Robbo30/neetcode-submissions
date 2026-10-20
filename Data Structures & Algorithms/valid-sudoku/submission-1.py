class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         elif board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])
        
        # for col in range(9):
        #     seen = set()
        #     for row in range(9):
        #         if board[row][col] == ".":
        #             continue
        #         elif board[row][col] in seen:
        #             return False
        #         seen.add(board[row][col])
        
        # for box_row in range(0, 9, 3):
        #     for box_col in range(0, 9, 3):
        #         seen = set()
        #         for row in range(box_row, box_row + 3):
        #             for col in range(box_col, box_col + 3):
        #                 item = board[row][col]
        #                 if item == ".":
        #                     continue
        #                 elif item in seen:
        #                     return False
        #                 seen.add(item)

        # return True



        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == ".":
                    continue
                elif item in rows[row]:
                    return False
                elif item in cols[col]:
                    return False
                elif item in squares[(row // 3, col // 3)]:
                    return False
                
                rows[row].add(item)
                cols[col].add(item)
                squares[(row // 3, col // 3)].add(item)
        
        return True

