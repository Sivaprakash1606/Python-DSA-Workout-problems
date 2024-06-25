# Dynamic Programming

"""
Fibonacci Series
1  2  3  4  5  6  7   8   9  - Position
1  1  2  3  5  8  13  21  34
"""


# Bottom up
def Fibo(position):
    if position <=2:
        print(1)
        return
    dp=[0]*position
    dp[0]=1
    dp[1]=1
    for i in range(2,position):
        dp[i]=dp[i-1]+dp[i-2]
    print(f"Fibo of {position}:{dp[-1]}")
Fibo(9)

#Top down
def Fibo(position,memory):
    if position in memory:
        return memory[position]
    if position <=2:
        return 1
    memory[position]=Fibo(position-1,memory)+Fibo(position-2,memory)
    print(memory.keys(),memory.values())
    return memory[position]
print(Fibo(5,{}))

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # Update dp[1] to be the maximum of nums[0] and nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Update dp[i] with the maximum of dp[i - 1] and dp[i - 2] + nums[i]
        return dp[-1]

nums =[1,5,1,1,2]
print(Solution().rob(nums))





