#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import List
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1

        def canFinish(piles, h, speed):
            time = 0
            for n in piles:
                time += (n // speed) + (1 if n % speed > 0 else 0)
            return time <= h

        while left < right:
            mid = left + (right - left) // 2
            if canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left

# @lc code=end
s = Solution()
s.minEatingSpeed([3, 6, 7, 11], 8)
