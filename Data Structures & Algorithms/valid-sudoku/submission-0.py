class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for r in row:
                if r == ".":
                    continue
                else:
                    if r in seen:
                        return False
                    else:
                        seen.add(r)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                else:
                    if num in seen:
                        return False
                    seen.add(num)
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = board[r][c]
                        if num == ".":
                            continue
                        else:
                            if num in seen:
                                return False
                            seen.add(num)
        
        return True