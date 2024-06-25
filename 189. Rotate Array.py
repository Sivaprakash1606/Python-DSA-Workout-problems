class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle thze case where k is greater than the length of nums

        # Instead of using while loop, we handle all rotations at once
        # The rightmost `k` elements will be moved to the front
        nums[:] = nums[-k:] + nums[:-k]

        return nums  # This return is not necessary as the problem states to modify in-place


# Example usage
sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))  # Output should be [5, 6, 7, 1, 2, 3, 4]
