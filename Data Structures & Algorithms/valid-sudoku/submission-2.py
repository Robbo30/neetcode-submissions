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
        #     for i in range(9):
        #         if board[i][col] == ".":
        #             continue
        #         elif board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])

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



        # Real Solution
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == ".":
                    continue
                elif item in rows[row] or item in cols[col] or item in boxes[(row // 3, col // 3)]:
                    return False
                rows[row].add(item)
                cols[col].add(item)
                boxes[(row // 3, col // 3)].add(item)
        
        return True