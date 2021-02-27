#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        capacity = 0
        for i in range(n - 1):
            capacity = max(capacity, i + nums[i])
            if capacity <= i: # 跳不动了，那就提前返回
                return False

        return capacity >= n - 1

# @lc code=end
