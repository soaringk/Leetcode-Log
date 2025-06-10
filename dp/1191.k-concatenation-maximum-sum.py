#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#
from typing import List
import math

# @lc code=start
class Solution:
    # 最长子数组，用前缀和的方式做
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.maxSubArray(arr)
        ans = self.maxSubArray(arr + arr)
        ans += max(sum(arr), 0) * (k - 2)
        return ans % 1_000_000_007


    # 右侧的最大前缀和减去左边最小前缀和
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0 # 本题允许子数组为空，ans 可以初始化成 0
        min_accu = accu = 0
        for x in nums:
            accu += x # 当前前缀和
            ans = max(ans, accu - min_accu)
            min_accu = min(min_accu, accu)
        return ans

# @lc code=end
Solution().kConcatenationMaxSum([-1,-2],7)
