class Solution:
    def findMaxK(self, nums) -> int:
        l=len(nums)
        m = max(nums)
        n = m - (2 * m)
        i = 0

        while i < l:
            if n in nums:
                return m
            elif m in nums:
                nums.remove(m)
                if nums:
                    m = max(nums)
                    print(m)
                    n = m - (2 * m)
                    print(n)
                else:
                    return -1
            i += 1

        return -1


nums = [-25,25,-27,45,31,46,46,21]
sol = Solution()
print(sol.findMaxK(nums))
