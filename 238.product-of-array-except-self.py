#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n  # 定义 pre[i] 表示从 nums[0] 到 nums[i−1] 的乘积。
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        suf = [1] * n  # 定义 suf[i] 表示从 nums[i+1] 到 nums[n−1] 的乘积。
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]


# @lc code=end
Solution().productExceptSelf([1,2,3,4])
