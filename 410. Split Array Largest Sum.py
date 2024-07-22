class Solution:
    def splitArray(self, nums, k):
        # maxx=0
        # distance=len(nums)//k
        # left=0
        # right=distance+1
        # i=1
        # while i<=distance:
        #     summ=0
        #     for j in range(left,right):
        #         summ=summ+nums[j]
        #     maxx=max(summ,maxx)
        #     left=right
        #     right=right+distance
        #     i=i+1
        # return maxx
nums = [7,2,5,10,8]
k = 2
print(Solution().splitArray(nums,k))