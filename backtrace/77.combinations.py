#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtack(start, end):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(start, end+1):
                path.append(i)
                backtack(i+1, end)
                path.pop()
        backtack(1, n)
        return ans
        
# @lc code=end
Solution().combine(4,2)