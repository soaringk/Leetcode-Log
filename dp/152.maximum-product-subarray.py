#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from typing import List
from math import inf


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 定义 f[i] 是以元素 i 结尾的最大乘积
        # f[i] = max(f[i-1] * nums[i], nums[i])
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            # 把 x 加到右端点为 i-1 的（乘积最大/最小）子数组后面，
            # 或者单独组成一个子数组，只有 x 一个元素
            dp_max[i] = max(dp_max[i - 1] * x, dp_min[i - 1] * x, x)
            dp_min[i] = min(dp_max[i - 1] * x, dp_min[i - 1] * x, x)
        return max(dp_max)


# @lc code=end
