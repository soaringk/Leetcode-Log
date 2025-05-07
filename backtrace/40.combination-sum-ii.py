#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        used = [False for _ in range(len(candidates))]
        def backtrack(start, target):
            if target == 0:
                ans.append(path[:])
                return
            if target < 0 or len(path) == len(candidates):
                return
            for i, cand in enumerate(candidates[start:]):
                if i > 0 and candidates[start+i] == candidates[start+i-1] and not used[start+i-1]:
                    continue
                path.append(cand)
                used[start+i] = True
                backtrack(start+i+1, target-cand)
                path.pop()
                used[start+i] = False
        backtrack(0, target)
        return ans
# @lc code=end
Solution().combinationSum2([10,1,2,7,6,1,5],8)