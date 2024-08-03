class Solution:
    def exist(self, board, word):
        def dfs(board, word, i, j, index):
            # Base case: If the current index equals the length of the word, we've found a match
            if index == len(word):
                return True

            # Check boundaries and whether the current cell matches the current character in the word
            if (i < 0 or i >= len(board) or
                    j < 0 or j >= len(board[0]) or
                    board[i][j] != word[index]):
                return False

            # Save the current cell's value and mark it as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore in all 4 directions
            found = (dfs(board, word, i + 1, j, index + 1) or
                     dfs(board, word, i - 1, j, index + 1) or
                     dfs(board, word, i, j + 1, index + 1) or
                     dfs(board, word, i, j - 1, index + 1))

            # Restore the cell's original value
            board[i][j] = temp
            return found

        # Start DFS from each cell in the grid
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True

        return False


# Test the solution with the provided input
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'A', 'S'],
    ['C', 'C', 'E', 'D']
]
word = "CCED"

# Create an instance of Solution and call the exist method
solution = Solution()
print(solution.exist(board, word))  # Output should be True
