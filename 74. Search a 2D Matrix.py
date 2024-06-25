class Solution:
    def searchMatrix(self,List ,target):
        n=len(matrix)//2
        if matrix[n][0]<target:
            for i in range(0,n):
                for j in range(len(matrix[i])):
                    if matrix[i][j]==target:
                        return True
                return False
        if matrix[n][0]<target:
            for i in range(n,len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j]==target:
                        return True
                return False
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(Solution().searchMatrix(matrix,target))