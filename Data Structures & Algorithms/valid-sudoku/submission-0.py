class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #the row 
        for i in range(len(board)):
            seen  = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False
        
        #check column

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False
        
        #check 3 by 3
        m = 0
        n = 0
        while m<9:
            while n<9:
                seen = set()
                for i in range(m, m+3):
                    for j in range(n, n+3):
                        if board[i][j] ==".":
                            continue
                        if board[i][j] not in seen:
                            seen.add(board[i][j])
                        else:
                            return False
                n+=3
            m+= 3

        return True


