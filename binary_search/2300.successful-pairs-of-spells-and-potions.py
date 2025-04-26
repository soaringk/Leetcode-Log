#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#
from typing import List

# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # binary search on spells
        potions.sort()
        pairs = [0] * len(spells)
        for i, spell in enumerate(spells):
            left = 0
            right = len(potions) - 1
            mid = left + (right - left) // 2
            # find first element greater that success
            while left <= right: # [left, right]

# @lc code=end
