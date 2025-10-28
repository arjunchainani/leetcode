def validateBoard(board, row, row_num):
    # given a board configuration, return True if it is valid (i.e. the queens will not attack each other)

    # if it's a repeat of something already in the board (i.e. same column) -> invalid
    # check for diagonals
    curr_x_pos = row.index('Q')
    curr_y_pos = row_num

    for index_num, prev_row in enumerate(board):
        prev_x_pos = prev_row.index('Q')
        prev_y_pos = index_num

        # if diagonal to existing queen -> invalid
        if curr_x_pos == prev_x_pos or (abs(curr_x_pos - prev_x_pos) == abs(curr_y_pos - prev_y_pos)):
            return False
    
    return True

def formatBoard(board):
    # do all the formatting and add the current board to the solutions list
    formatted = board[:]
    for index, row in enumerate(formatted):
        formatted[index] = "".join(row)
    
    return formatted

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []

        def dfs(board, row_num):
            # base case 2: finished the board
            if row_num == n:
                formatted = formatBoard(board) # logic may need to be fleshed out depending on the structure of board
                solutions.append(formatted)
                return
            
            # recursive cases
            for i in range(n):
                new_row = ['.'] * i + ['Q'] + ['.'] * (n - i - 1)
                
                # checks to avoid adding new rows if that involves queens in the same column
                if validateBoard(board, new_row, row_num):
                    board.append(new_row)
                    dfs(board, row_num + 1)
                    board.pop()
        
        dfs([], 0)
        return solutions