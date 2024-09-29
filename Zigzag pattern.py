def isZMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            # Check for first row, last row, main diagonal, and anti-diagonal
            if (i == 0 or i == rows - 1 or j == cols - i - 1):
                if matrix[i][j] == 0:
                    return False
            else:
                # All other elements should be zero
                if matrix[i][j] != 0:
                    return False

    return True


# Test with the specific input
print(isZMatrix([[1, 2, 3, 4],
               [0, 0, 3, 0],
               [0, 2,0, 0],
               [1, 2, 3, 4]]))  # Output: False


