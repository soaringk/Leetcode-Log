#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights) + 1

        def canFinish(weights, D, cap):
            w = 0
            for _ in range(D):
                max_cap = cap
                while max_cap - weights[w] >= 0:
                    max_cap -= weights[w]
                    w += 1
                    if w == len(weights):
                        return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if canFinish(weights, D, mid):
                right = mid
            else:
                left = mid + 1

        return left

# @lc code=end
