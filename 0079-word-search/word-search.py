# backtracking approach: start with an initial board position
# from here, you can either move left, right, up, or down (but check that you don't go off the board)
# also keep track of the current index in the string, if index > word len check if word matches and otherwise reject
# otherwise check if the current char matches, if not, backtrack
# also need a visited list to make sure that you don't check the same character again, if all neighbors visited, backtrack

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # optimization: if we don't have enough letters, don't bother
        board_count = Counter(char for row in board for char in row)
        word_count = Counter(word)
    
        for count in word_count:
            if word_count[count] > board_count.get(count, 0):
                return False

        def check_on_board(position, board_len, board_height):
            if position[0] < 0 or position[1] < 0:
                return False
            elif position[0] >= board_len:
                return False
            elif position[1] >= board_height:
                return False
            else:
                return True
        
        def dfs(position, index):
            if board[position[1]][position[0]] != word[index]:
                return False
            if index == len(word) - 1 and board[position[1]][position[0]] == word[index]:
                return True
            
            delta_x = [-1, 0, 1, 0]
            delta_y = [0, 1, 0, -1]

            current_char = board[position[1]][position[0]] 
            board[position[1]][position[0]] = '*'
            
            for neighbor_x, neighbor_y in zip(delta_x, delta_y):
                updated_pos = (position[0] + neighbor_x, position[1] + neighbor_y)
                
                if check_on_board(updated_pos, len(board[0]), len(board)):
                    if dfs(updated_pos, index + 1):
                        return True

            board[position[1]][position[0]] = current_char
            return False

        # optimization: if last letter is rarer than first letter, search for the word in reverse (reduces the number of possible paths)
        if board_count[word[-1]] < board_count[word[0]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs((j, i), 0):
                    return True
        
        return False