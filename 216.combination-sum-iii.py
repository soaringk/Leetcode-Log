#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum3Complex(self, k: int, n: int) -> List[List[int]]:
        ans = []

        options = [x for x in range(1,10)]
        def backtrack(path: List[int], options: List[int], k: int, n: int):
            if n == 0 and k == 0:
                ans.append(path[:])
                return
            if n < 0 or k < 0:
                return
            for i, x in enumerate(options):
                path.append(x)
                backtrack(path, options[i+1:], k-1, n-x)
                path.pop()
        backtrack([], options, k, n)
        return ans

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(start: int, k: int, n: int):
            if n == 0 and k == 0:
                ans.append(path[:])
                return
            if n < 0 or k < 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i+1, k-1, n-i)
                path.pop()
        backtrack(1, k, n)
        return ans
# @lc code=end
Solution().combinationSum3(3, 7)
