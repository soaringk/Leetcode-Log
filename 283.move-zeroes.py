#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack_size = 0
        for x in nums:
            if x != 0:
                nums[stack_size] = x
                stack_size += 1
        for i in range(stack_size, len(nums)):
            nums[i] = 0


# @lc code=end
