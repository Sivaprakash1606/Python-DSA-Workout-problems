class Solution:
    def spiralOrder(self, matrix):
        result = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row from left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            # Traverse rightmost column from top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row from right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Traverse leftmost column from bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
matrix=[[1,2,3],[4,5,6],[7,8,9],[0,1,2]]
print(Solution().spiralOrder(matrix))